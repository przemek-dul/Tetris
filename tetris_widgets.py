import pygame


class Widgets:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Comic Sans MS', 24)
        self.font_2 = pygame.font.SysFont('Comic Sans MS', 36)
        self.font_3 = pygame.font.SysFont('Comic Sans MS', 22)
        self.level = 1
        self.score = 0
        self.score_buffer = 0
        self.lines = 0
        self.rectangles = []

        self.level_text = self.font.render(f"LEVEL {self.level}", False, (203, 197, 199))
        self.score_text = self.font.render(f"SCORE {self.score}", False, (203, 197, 199))
        self.lines_text = self.font.render(f"LINES {self.lines}", False, (203, 197, 199))
        self.start_text = self.font_2.render("GRAJ", False, (203, 197, 199))
        self.reset_text = self.font_3.render("Zagraj jeszcze raz", False, (203, 197, 199))
        self.result = self.font_2.render("Twój wynik to:", False, (0, 107, 48))
        self.result_info = self.font_2.render(f"{self.score_buffer}", False, (0, 107, 48))

        self.vector = []
        self.block = self.block = pygame.image.load("red_block.png")
        self.create()
        self.start_btn = pygame.Rect(120, 150, 240, 100)
        self.reset_btn = pygame.Rect(120, 300, 240, 100)

        self.first = "1."
        self.second = "2."
        self.third = "3."
        self.fourth = "4."
        self.fifth = "5."

        self.high_score = ""

        self.place_1 = self.font_2.render(self.first, False, (0, 107, 48))
        self.place_2 = self.font_2.render(self.second, False, (0, 107, 48))
        self.place_3 = self.font_2.render(self.third, False, (0, 107, 48))
        self.place_4 = self.font_2.render(self.fourth, False, (0, 107, 48))
        self.place_5 = self.font_2.render(self.fifth, False, (0, 107, 48))

        self.new_best = self.font_2.render(self.high_score, False, (0, 107, 48))

    def create(self):
        for position in self.vector:
            self.rectangles.append(self.block.get_rect(topleft=(position[0], position[1])))

    def info(self):
        self.level_text = self.font.render(f"LEVEL {self.level}", False, (203, 197, 199))
        self.score_text = self.font.render(f"SCORE {self.score}", False, (203, 197, 199))
        self.lines_text = self.font.render(f"LINES {self.lines}", False, (203, 197, 199))

        pygame.draw.line(self.screen, (203, 197, 199), (500, 35), (750, 35), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (500, 35), (500, 180), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (500, 180), (750, 180), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (750, 180), (750, 35), 5)

        pygame.draw.line(self.screen, (203, 197, 199), (500, 220), (750, 220), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (500, 220), (500, 400), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (500, 400), (750, 400), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (750, 400), (750, 220), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (500, 280), (750, 280), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (500, 340), (750, 340), 5)

        self.screen.blit(self.level_text, (520, 230))
        self.screen.blit(self.score_text, (520, 290))
        self.screen.blit(self.lines_text, (520, 350))

    def next_shape(self):
        for rectangle in self.rectangles:
            self.screen.blit(self.block, rectangle)

    def draw_all(self):
        self.info()
        self.next_shape()

    def start_menu(self):
        self.place_1 = self.font_2.render(self.first, False, (0, 107, 48))
        self.place_2 = self.font_2.render(self.second, False, (0, 107, 48))
        self.place_3 = self.font_2.render(self.third, False, (0, 107, 48))
        self.place_4 = self.font_2.render(self.fourth, False, (0, 107, 48))
        self.place_5 = self.font_2.render(self.fifth, False, (0, 107, 48))

        pygame.draw.rect(self.screen, (255, 255, 255), (60, 60, 360, 640))
        pygame.draw.line(self.screen, (203, 197, 199), (60, 60), (420, 60), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (60, 60), (60, 700), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (60, 700), (420, 700), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (420, 60), (420, 700), 5)

        pygame.draw.rect(self.screen, (21, 24, 33), (120, 150, 240, 100))
        pygame.draw.line(self.screen, (203, 197, 199), (120, 150), (360, 150), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (120, 150), (120, 250), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (120, 250), (360, 250), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (360, 250), (360, 150), 5)

        self.screen.blit(self.start_text, (190, 170))

        self.screen.blit(self.place_1, (120, 320))
        self.screen.blit(self.place_2, (120, 360))
        self.screen.blit(self.place_3, (120, 400))
        self.screen.blit(self.place_4, (120, 440))
        self.screen.blit(self.place_5, (120, 480))

    def defeat(self):
        self.result_info = self.font_2.render(f"{self.score_buffer}", False, (0, 107, 48))
        self.place_1 = self.font_2.render(self.first, False, (0, 107, 48))
        self.place_2 = self.font_2.render(self.second, False, (0, 107, 48))
        self.place_3 = self.font_2.render(self.third, False, (0, 107, 48))
        self.place_4 = self.font_2.render(self.fourth, False, (0, 107, 48))
        self.place_5 = self.font_2.render(self.fifth, False, (0, 107, 48))

        self.new_best = self.font_2.render(self.high_score, False, (0, 107, 48))

        pygame.draw.rect(self.screen, (255, 255, 255), (60, 60, 360, 640))
        pygame.draw.line(self.screen, (203, 197, 199), (60, 60), (420, 60), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (60, 60), (60, 700), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (60, 700), (420, 700), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (420, 60), (420, 700), 5)

        pygame.draw.rect(self.screen, (21, 24, 33), (120, 300, 240, 100))
        pygame.draw.line(self.screen, (203, 197, 199), (120, 300), (360, 300), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (120, 300), (120, 400), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (120, 400), (360, 400), 5)
        pygame.draw.line(self.screen, (203, 197, 199), (360, 400), (360, 300), 5)

        self.screen.blit(self.reset_text, (140, 330))
        self.screen.blit(self.result, (130, 100))
        self.screen.blit(self.result_info, (230, 160))

        self.screen.blit(self.place_1, (120, 420))
        self.screen.blit(self.place_2, (120, 460))
        self.screen.blit(self.place_3, (120, 500))
        self.screen.blit(self.place_4, (120, 540))
        self.screen.blit(self.place_5, (120, 580))
        self.screen.blit(self.new_best, (150, 200))



