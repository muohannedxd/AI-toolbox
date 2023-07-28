import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
# Colors
LIGHT_SQUARE_COLOR = (232, 232, 232)
DARK_SQUARE_COLOR = (50, 50, 50)
RED_COLOR = (255, 0, 0)
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
HIGHLIGHT_COLOR = (0, 255, 0)


CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
