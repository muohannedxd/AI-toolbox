import pygame
from pygame.locals import *

from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_COLOR = (0, 0, 255)
BUTTON_TEXT = "Quit"
BUTTON_TEXT_COLOR = (255, 255, 255)

# Adjusted screen dimensions
SCREEN_WIDTH = WIDTH + BUTTON_WIDTH + 20
SCREEN_HEIGHT = HEIGHT

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Checkers')

quit_button_rect = pygame.Rect(WIDTH + 10, HEIGHT - 2 * BUTTON_HEIGHT - 20, BUTTON_WIDTH, BUTTON_HEIGHT)
restart_button_rect = pygame.Rect(WIDTH + 10, HEIGHT - BUTTON_HEIGHT - 10, BUTTON_WIDTH, BUTTON_HEIGHT)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_buttons():
    pygame.draw.rect(WIN, BUTTON_COLOR, quit_button_rect)
    pygame.draw.rect(WIN, BUTTON_COLOR, restart_button_rect)

    font = pygame.font.Font(None, 24)
    quit_text = font.render("Quit", True, BUTTON_TEXT_COLOR)
    quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
    WIN.blit(quit_text, quit_text_rect)

    restart_text = font.render("Restart", True, BUTTON_TEXT_COLOR)
    restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
    WIN.blit(restart_text, restart_text_rect)


def is_button_clicked(pos, button_rect):
    return button_rect.collidepoint(pos)


def main():
    pygame.init()
    pygame.font.init()
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    depth = 2

    draw_buttons()

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, float('-inf'), float('inf'), WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if is_button_clicked(pos, quit_button_rect):
                    run = False
                elif is_button_clicked(pos, restart_button_rect):
                    game.reset()
                else:
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        game.update()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
