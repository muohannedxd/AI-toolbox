from .constants import SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        outline_radius = radius + self.OUTLINE
        pygame.draw.circle(win, GREY, (self.x, self.y), outline_radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            crown_x = self.x - CROWN.get_width() // 2
            crown_y = self.y - CROWN.get_height() // 2
            win.blit(CROWN, (crown_x, crown_y))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
