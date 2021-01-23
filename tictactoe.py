"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    AI is O, user is X
    """   
    X_count = 0
    O_count = 0
    for _, row in enumerate(board):
        for _, col in enumerate(row):
            if col == X:
                X_count += 1
            elif col == O:
                O_count += 1
    # if the board is empty, first move is made by user
    if X_count == 0 and O_count == 0:
        first_move = X
        return X
    # if there are more Xs than Os next player is O
    elif X_count > O_count:
        return O
    # If there are equal or more Os than Xs next player is X
    else:
        return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                possible.add((i, j))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception('Cell is not empty!')
    next_player = player(board)
    new_board = deepcopy(board)
    new_board[i][j] = next_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    global game_winner
    winning_triplets = [
        ((0, 0), (0, 1), (0, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((2, 0), (1, 1), (0, 2))
    ]
    for triplet in winning_triplets:
        current = []
        for point in triplet:
            current.append(board[point[0]][point[1]])
        if current[0] != EMPTY and all(el==current[0] for el in current):
            game_winner = current[0]
            return current[0]
    
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_won = winner(board) != None
    is_filled = all(col != EMPTY for i, row in enumerate(board) 
                    for j, col in enumerate(row))
    return is_won or is_filled


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == None:
        return 0
    elif game_winner == X:
        return 1
    else:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if not terminal(board):
        current_player = player(board)
        if current_player is O:
            print("O's turn")
        if current_player == X:
            v, action = max_value(board)
        else:
            v, action = min_value(board)
        return action
            

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -100000
    optimal_action = None
    for action in actions(board):
        current_value = min_value(result(board, action))[0]

        if current_value >= v:
            optimal_action = action
            v = current_value
    return v, optimal_action


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = 10000
    optimal_action = None
    for action in actions(board):
        current_value = max_value(result(board, action))[0]
        
        if current_value <= v:
            v = current_value
            optimal_action = action
            
    return v, optimal_action
