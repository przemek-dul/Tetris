import pygame
import random
import time


class Shape1:
    def __init__(self, screen):
        self.xy = [[160, 0], [200, 0], [240, 0], [280, 0]]
        self.screen = screen
        self.color = random.randint(0, 5)
        self.block = None
        self.move = True
        self.right = False
        self.left = False
        self.fast_drop = False
        self.drop_limit = 0
        self.poz = 1
        self.speed = 1.5

        self.rectangles = []
        self.time = 0
        self.left_press = False
        self.right_press = False
        self.r_clicked = False
        self.l_clicked = False
        self.limit_right = 0
        self.limit_left = 0

        self.maxRotations = 2

        self.load()
        self.create()

    def load(self):
        if self.color == 0:
            self.block = pygame.image.load("textures/red_block.png")
        if self.color == 1:
            self.block = pygame.image.load("textures/blue_block.png")
        if self.color == 2:
            self.block = pygame.image.load("textures/yellow_block.png")
        if self.color == 3:
            self.block = pygame.image.load("textures/green_block.png")
        if self.color == 4:
            self.block = pygame.image.load("textures/violet_block.png")
        if self.color == 5:
            self.block = pygame.image.load("textures/orange_block.png")

    def create(self):
        for position in self.xy:
            self.rectangles.append(self.block.get_rect(topleft=(position[0], position[1])))

    def moving(self):
        if self.move and not self.fast_drop and self.drop_limit < time.time():
            self.drop_limit = time.time() + self.speed
            for rectangle in self.rectangles:
                rectangle.y += 40
        if self.move and self.fast_drop and self.drop_limit < time.time():
            self.drop_limit = time.time() + 0.05
            for rectangle in self.rectangles:
                rectangle.y += 40

    def display(self):
        for rectangle in self.rectangles:
            self.screen.blit(self.block, rectangle)
        self.turn()
        self.moving()

    def turn(self):

        if self.right and not self.r_clicked:
            self.r_clicked = True
            self.limit_right = time.time() + 0.25
            for rectangle in self.rectangles:
                rectangle.x += 40
        if self.left and not self.l_clicked:
            self.l_clicked = True
            self.limit_left = time.time() + 0.25
            for rectangle in self.rectangles:
                rectangle.x -= 40

        if self.right and self.r_clicked and self.limit_right <= time.time():
            self.limit_right = time.time() + 0.1
            for rectangle in self.rectangles:
                rectangle.x += 40
        if self.left and self.l_clicked and self.limit_left <= time.time():
            self.limit_left = time.time() + 0.1
            for rectangle in self.rectangles:
                rectangle.x -= 40

    def rotation(self):
        if self.poz == 1:
            self.rectangles[0].x += 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y += 40
            self.rectangles[3].x -= 80
            self.rectangles[3].y += 80
            self.poz = 2
            return 0
        if self.poz == 2:
            self.rectangles[0].x -= 40
            self.rectangles[0].y += 40
            self.rectangles[2].x += 40
            self.rectangles[2].y -= 40
            self.rectangles[3].x += 80
            self.rectangles[3].y -= 80
            self.poz = 1
            return 0


class Shape2(Shape1):
    def __init__(self, screen):
        super(Shape2, self).__init__(screen=screen)
        self.xy = [[160, 0], [200, 0], [240, 0], [200, 40]]
        self.rectangles.clear()
        self.create()
        self.maxRotations = 4

    def rotation(self):
        if self.poz == 1:
            self.rectangles[0].x += 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y += 40
            self.rectangles[3].x -= 40
            self.rectangles[3].y -= 40
            self.poz = 2
            return 0
        if self.poz == 2:
            self.rectangles[0].x += 40
            self.rectangles[0].y += 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y -= 40
            self.rectangles[3].x += 40
            self.rectangles[3].y -= 40
            self.poz = 3
            return 0
        if self.poz == 3:
            self.rectangles[0].x -= 40
            self.rectangles[0].y += 40
            self.rectangles[2].x += 40
            self.rectangles[2].y -= 40
            self.rectangles[3].x += 40
            self.rectangles[3].y += 40
            self.poz = 4
            return 0
        if self.poz == 4:
            self.rectangles[0].x -= 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x += 40
            self.rectangles[2].y += 40
            self.rectangles[3].x -= 40
            self.rectangles[3].y += 40
            self.poz = 1
            return 0


class Shape3(Shape1):
    def __init__(self, screen):
        super(Shape3, self).__init__(screen=screen)
        self.xy = [[200, 40], [200, 0], [240, 0], [240, 40]]
        self.rectangles.clear()
        self.create()
        self.maxRotations = 2

    def rotation(self):
        pass


class Shape4(Shape1):
    def __init__(self, screen):
        super(Shape4, self).__init__(screen=screen)
        self.xy = [[160, 40], [200, 40], [240, 40], [240, 0]]
        self.rectangles.clear()
        self.create()
        self.maxRotations = 4

    def rotation(self):
        if self.poz == 1:
            self.rectangles[0].x += 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y += 40
            self.rectangles[3].y += 80
            self.poz = 2
            return 0
        if self.poz == 2:
            self.rectangles[0].x += 40
            self.rectangles[0].y += 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y -= 40
            self.rectangles[3].x -= 80
            self.poz = 3
            return 0
        if self.poz == 3:
            self.rectangles[0].x -= 40
            self.rectangles[0].y += 40
            self.rectangles[2].x += 40
            self.rectangles[2].y -= 40
            self.rectangles[3].y -= 80
            self.poz = 4
            return 0
        if self.poz == 4:
            self.rectangles[0].x -= 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x += 40
            self.rectangles[2].y += 40
            self.rectangles[3].x += 80
            self.poz = 1
            return 0


class Shape5(Shape1):
    def __init__(self, screen):
        super(Shape5, self).__init__(screen=screen)
        self.xy = [[160, 0], [200, 0], [240, 0], [240, 40]]
        self.rectangles.clear()
        self.create()
        self.maxRotations = 4

    def rotation(self):
        if self.poz == 1:
            self.rectangles[0].x += 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y += 40
            self.rectangles[3].x -= 80
            self.poz = 2
            return 0
        if self.poz == 2:
            self.rectangles[0].x += 40
            self.rectangles[0].y += 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y -= 40
            self.rectangles[3].y -= 80
            self.poz = 3
            return 0
        if self.poz == 3:
            self.rectangles[0].x -= 40
            self.rectangles[0].y += 40
            self.rectangles[2].x += 40
            self.rectangles[2].y -= 40
            self.rectangles[3].x += 80
            self.poz = 4
            return 0
        if self.poz == 4:
            self.rectangles[0].x -= 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x += 40
            self.rectangles[2].y += 40
            self.rectangles[3].y += 80
            self.poz = 1
            return 0


class Shape6(Shape1):
    def __init__(self, screen):
        super(Shape6, self).__init__(screen=screen)
        self.xy = [[160, 40], [200, 40], [200, 0], [240, 0]]
        self.rectangles.clear()
        self.create()
        self.maxRotations = 2

    def rotation(self):
        if self.poz == 1:
            self.rectangles[0].x += 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x += 40
            self.rectangles[2].y += 40
            self.rectangles[3].y += 80
            self.poz = 2
            return 0
        if self.poz == 2:
            self.rectangles[0].x -= 40
            self.rectangles[0].y += 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y -= 40
            self.rectangles[3].y -= 80
            self.poz = 1
            return 0


class Shape7(Shape1):
    def __init__(self, screen):
        super(Shape7, self).__init__(screen=screen)
        self.xy = [[160, 0], [200, 0], [200, 40], [240, 40]]
        self.rectangles.clear()
        self.create()
        self.maxRotations = 2

    def rotation(self):
        if self.poz == 1:
            self.rectangles[0].x += 40
            self.rectangles[0].y -= 40
            self.rectangles[2].x -= 40
            self.rectangles[2].y -= 40
            self.rectangles[3].x -= 80
            self.poz = 2
            return 0
        if self.poz == 2:
            self.rectangles[0].x -= 40
            self.rectangles[0].y += 40
            self.rectangles[2].x += 40
            self.rectangles[2].y += 40
            self.rectangles[3].x += 80
            self.poz = 1
            return 0
