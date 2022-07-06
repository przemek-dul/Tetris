class Settings:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.speed = 1.5
        self.level = 1
        self.levels = {1: 1.5, 2: 1.4, 3: 1.3, 4: 1.2, 5: 1.1, 6: 1, 7: 0.95, 8: 0.9, 9: 0.85, 10: 0.8, 11: 0.75,
                       12: 0.7, 13: 0.65, 14: 0.6, 15: 0.55, 16: 0.5, 17: 0.45, 18: 0.4, 19: 0.35, 20: 0.3, 21: 0.25,
                       22: 0.24, 23: 0.23, 24: 0.22, 25: 0.21, 26: 0.20, 27: 0.19, 28: 0.18, 29: 0.17}
        self.speed = self.levels[self.level]
        self.changes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210,
                        220, 230, 240, 250, 260, 270, 280, 290]
        self.it = 0

    def level_inc(self, lines):
        if self.level < 28:
            if lines == self.changes[self.it]:
                self.level += 1
                self.it += 1
