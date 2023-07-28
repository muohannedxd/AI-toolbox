from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

# position = it's a board object. This is the current board configuration. Given the current board configuration
# the minimax should provide the optimal board configuration (best board configuration) as we play.

# depth = how far we are extending the minimax tree. Everytime we evaluate the algorithm,
# we will decrease the depth by 1. Remember: we only evaluate a position when we reach the end of the tree (root node).

# max_player = boolean value (True/False) that tells us if we are maximizing or minimizing the reward.
# If max_player is TRUE, we tend to maximize our rewards.

#game = this is the game object from main.py. It is used to draw and update the board as we play.

def minimax(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if maxEval == evaluation:
                best_move = move
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if minEval == evaluation:
                best_move = move
            if beta <= alpha:
                break
        return minEval, best_move

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves



def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)


