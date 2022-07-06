import pygame
from Tetris_set import Settings
import sys
import shapes
import random
from tetris_widgets import Widgets
import json


class Tetris:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.current_figure = self.shape_generator()
        self.current_figure.speed = self.settings.levels[self.settings.level]
        self.next_figure = self.shape_generator()
        self.delay = 0
        self.collision = 0
        self.widget = Widgets(self.screen)
        self.widget.vector = self.future()
        self.widget.create()
        self.widget.level = self.settings.level

        self.run_game = False
        self.start_menu = True
        self.lose = False
        self.rectangles = []

        record = self.open_record()
        self.show_records(record)

        self.main()

    def main(self):
        while True:
            if self.run_game:
                self.event_check()
                self.collisions()
                self.side_collisions()
                self.current_figure.display()
                self.screen_update()

            if self.start_menu:
                self.event_check_start_menu()
                self.clock.tick(60)
                self.screen.fill((255, 255, 255))
                self.board()
                self.draw_rectangles()
                self.widget.info()
                self.widget.start_menu()
                pygame.display.update()

            if self.lose:
                self.event_check_start_menu()
                self.clock.tick(60)
                self.screen.fill((255, 255, 255))
                self.board()
                self.draw_rectangles()
                self.widget.info()
                self.widget.defeat()
                pygame.display.update()

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.current_figure.right_press = True
                    self.current_figure.right = True
                if event.key == pygame.K_LEFT:
                    self.current_figure.left_press = True
                    self.current_figure.left = True
                if event.key == pygame.K_DOWN:
                    self.current_figure.drop_limit = 0
                    self.current_figure.fast_drop = True
                if event.key == pygame.K_UP:
                    self.current_figure.rotation()
                    if not self.let_me_round():
                        for i in range(1, self.current_figure.maxRotations):
                            self.current_figure.rotation()
                    else:
                        pass

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.current_figure.fast_drop = False
                if event.key == pygame.K_RIGHT:
                    self.current_figure.right = False
                    self.current_figure.right_press = False
                    self.current_figure.r_clicked = False
                if event.key == pygame.K_LEFT:
                    self.current_figure.left = False
                    self.current_figure.left_press = False
                    self.current_figure.l_clicked = False

    def event_check_start_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.start_menu:
                mouse_pos = pygame.mouse.get_pos()
                if self.widget.start_btn.collidepoint(mouse_pos):
                    self.run_game = True
                    self.start_menu = False

            if event.type == pygame.MOUSEBUTTONDOWN and self.lose:
                mouse_pos = pygame.mouse.get_pos()
                if self.widget.reset_btn.collidepoint(mouse_pos):
                    self.run_game = True
                    self.lose = False
                    self.widget.high_score = ''

    def board(self):
        pygame.draw.line(self.screen, (203, 197, 199), (35, 35), (35, 765), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (35, 35), (445, 35), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (445, 35), (445, 765), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (445, 765), (35, 765), 5)
        pygame.draw.rect(self.screen, (21, 24, 33), (40, 40, 400, 720))

        x_start = 80
        y_start = 40
        for k in range(0, 9):
            pygame.draw.line(self.screen, (203, 197, 199), (x_start, 35), (x_start, 765))
            x_start += 40
        for k in range(0, 18):
            pygame.draw.line(self.screen, (203, 197, 199), (35, y_start), (445, y_start))
            y_start += 40

    def screen_update(self):
        self.clock.tick(60)
        self.screen.fill((255, 255, 255))
        self.board()
        self.draw_rectangles()
        self.widget.draw_all()
        self.current_figure.display()
        pygame.display.update()

    def shape_generator(self):
        figura = random.choice([shapes.Shape1(self.screen), shapes.Shape2(self.screen),
                                shapes.Shape3(self.screen), shapes.Shape4(self.screen),
                                shapes.Shape5(self.screen), shapes.Shape6(self.screen),
                                shapes.Shape7(self.screen)])
        return figura

    def draw_rectangles(self):
        for rectangle in self.rectangles:
            self.screen.blit(rectangle[1], rectangle[0])

    def collisions(self):
        if self.collision == 0:
            for rectangle in self.current_figure.rectangles:
                if rectangle.centery > 740:
                    self.current_figure.move = False
                    for k in self.current_figure.rectangles:
                        k.y -= 40
                        self.rectangles.append((k, self.current_figure.block))
                    self.defeat()
                    self.check_minus()
                    self.keep_moving()
                    self.current_figure = self.next_figure
                    self.current_figure.speed = self.settings.levels[self.settings.level]
                    self.next_figure = self.shape_generator()
                    self.widget.vector = self.future()
                    self.widget.create()
                    return 0

                for block in self.rectangles:
                    if block[0].y < rectangle.y + 40 < block[0].y + 42 and block[0].x == rectangle.x:
                        self.current_figure.move = False
                        for k in self.current_figure.rectangles:
                            k.y -= 40
                            self.rectangles.append((k, self.current_figure.block))
                        self.defeat()
                        self.check_minus()
                        self.keep_moving()
                        self.current_figure = self.next_figure
                        self.current_figure.speed = self.settings.levels[self.settings.level]
                        self.next_figure = self.shape_generator()
                        self.widget.vector = self.future()
                        self.widget.create()
                        return 0

    def side_collisions(self):
        for rectangle in self.current_figure.rectangles:
            if rectangle.x <= 75 and self.current_figure.left_press:
                self.current_figure.left = False
            if rectangle.x >= 395 and self.current_figure.right_press:
                self.current_figure.right = False
            for pros in self.rectangles:
                if pros[0].y == rectangle.y and pros[0].x == rectangle.x - 40 and self.current_figure.left_press:
                    self.current_figure.left = False
                if pros[0].y == rectangle.y and pros[0].x == rectangle.x + 40 and self.current_figure.right_press:
                    self.current_figure.right = False

    def let_me_round(self):
        for rectangle in self.current_figure.rectangles:
            if rectangle.x < 75 - 40:
                return False
            if rectangle.x > 395 + 40:
                return False
            if rectangle.y >= 740:
                return False
            if rectangle.y < 40:
                return False
            for pros in self.rectangles:
                if pros[0].x == rectangle.x and pros[0].y == rectangle.y:
                    return False
        return True

    def check_minus(self):
        combo = 0
        points = 0
        for i in range(1, 19):
            number = 0
            poten = []
            for rectangle in self.rectangles:
                if rectangle[0].y == i * 40:
                    number += 1
                    poten.append(rectangle)
            if number == 10:
                combo += 1
                points += 10
                self.widget.lines += 1
                self.settings.level_inc(self.widget.lines)
                self.widget.level = self.settings.level
                for k in poten:
                    self.rectangles.remove(k)
                for k in self.rectangles:
                    if k[0].y < i * 40:
                        k[0].y += 40
            self.widget.score += (combo * points * self.settings.level)

    def future(self):
        vector = self.next_figure.xy
        self.widget.block = self.next_figure.block
        self.widget.rectangles.clear()
        for k in vector:
            k[0] += 390
            k[1] += 60
        return vector

    def defeat(self):
        for rectangle in self.current_figure.rectangles:
            if rectangle.y == 0:
                self.widget.score_buffer = self.widget.score
                record = self.open_record()
                new_record = self.save_new_record(record)
                if new_record:
                    self.widget.high_score = 'NEW BEST!!!'
                record = self.open_record()
                self.show_records(record)
                self.run_game = False
                self.lose = True
                self.rectangles.clear()
                self.widget.lines = 0
                self.settings.level = 1
                self.widget.score = 0
                self.widget.level = 1
                self.current_figure = self.shape_generator()
                return 0

    def keep_moving(self):
        if self.current_figure.fast_drop:
            self.next_figure.fast_drop = True
        if self.current_figure.r_clicked:
            self.next_figure.r_clicked = True
            self.next_figure.right = True
            self.next_figure.right_press = True

        if self.current_figure.l_clicked:
            self.next_figure.l_clicked = True
            self.next_figure.left = True
            self.next_figure.left_press = True

    def open_record(self):
        with open("rekordy.json", "r") as file:
            record = json.load(file)
        return record

    def show_records(self, record):
        self.widget.first = '1.' + str(record['1'])
        self.widget.second = '2.' + str(record['2'])
        self.widget.third = '3.' + str(record['3'])
        self.widget.fourth = '4.' + str(record['4'])
        self.widget.fifth = '5.' + str(record['5'])

    def save(self, record):
        with open("rekordy.json", "w") as file:
            json.dump(record, file)

    def save_new_record(self, record):
        if self.widget.score > int(record['1']):
            record['5'] = record['4']
            record['4'] = record['3']
            record['3'] = record['2']
            record['2'] = record['1']
            record['1'] = self.widget.score
            self.save(record)
            return True
        if self.widget.score > int(record['2']):
            record['5'] = record['4']
            record['4'] = record['3']
            record['3'] = record['2']
            record['2'] = self.widget.score
            self.save(record)
            return False
        if self.widget.score > int(record['3']):
            record['5'] = record['4']
            record['4'] = record['3']
            record['3'] = self.widget.score
            self.save(record)
            return False
        if self.widget.score > int(record['4']):
            record['5'] = record['4']
            record['4'] = self.widget.score
            self.save(record)
            return False
        if self.widget.score > int(record['5']):
            record['5'] = self.widget.score
            self.save(record)
            return False
        else:
            return False


gra = Tetris()
