# Title:  Connect Four
# Author:  Ryan Hawkins

import random
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def create_board():
    board = {}
    for row in range(6):
        for column in range(7):
            board[(row, column)] = EMPTY
    return board




EMPTY = "   "
WIN_SYMBOL = "WON"
COMPUTER = "CP"
board = create_board()

# BOARD_WIDTH = 6
# BOARD_HEIGHT = 7




def display_board(board):
    labels = []
    for row in range(6):
        for column in range(7):
            labels.append(str(board[(row, column)]).center(3))
    display_title("connect four")
    print("""
  1   2   3   4   5   6   7
.   .   .   .   .   .   .  .
|{}|{}|{}|{}|{}|{}|{}|
+---+---+---+---+---+---+---+
|{}|{}|{}|{}|{}|{}|{}|
+---+---+---+---+---+---+---+
|{}|{}|{}|{}|{}|{}|{}|
+---+---+---+---+---+---+---+
|{}|{}|{}|{}|{}|{}|{}|
+---+---+---+---+---+---+---+
|{}|{}|{}|{}|{}|{}|{}|
+---+---+---+---+---+---+---+
|{}|{}|{}|{}|{}|{}|{}|
+--- --- --- --- --- --- ---+
""".format(*labels))


def play_turn(player):
    clear()
    display_board(board)
    column_choice = input(f"Player {player}, place your piece (1-7): ")
    valid_choice = False
    while not valid_choice:
        while column_choice not in ["1", "2", "3", "4", "5", "6", "7", "reset"]:
            if column_choice is reset:
                reset_game()
            column_choice = input("Choose from 1 to 7: ")

        column = int(column_choice) - 1
        if board[(0, column)] == EMPTY:
            valid_choice = True
        else:
            valid_choice = False
            column_choice = input("That column is full. Choose another one: ")

    drop_piece(player, column)
    #display_board(board)


def computer_turn(board, player):
    # computer randomly chooses from available columns
    available_columns = []
    time.sleep(.5)
    for column in range(7):
        if board[(0, column)] == EMPTY:
            available_columns.append(column)
    column_choice = random.choice(available_columns)
    drop_piece(player, column_choice)


def column_full(column):
    if board[(0, column)] == EMPTY:
        return False
    return True


def board_full(board):
    for row in range(6):
        for column in range(7):
            if board[(row, column)] == EMPTY:
                return False
    return True


def drop_piece(player, column):
    row = 6
    placed = False
    while not placed:
        row -= 1
        if board[(row, column)] == EMPTY:
            board[(row, column)] = player
            placed = True


def game_won(board):
    if horizontal_win(board):
        return True
    if vertical_win(board):
        return True
    if diagonal_win(board):
        return True

    return False


def horizontal_win(board):
    for row in range(6):
        for column in range(4):  # Limited columns to avoid KeyError
            if board[(row, column)] == board[(row, column + 1)] == board[(
                    row, column + 2)] == board[(row, column + 3)] != EMPTY:
                board[(row, column)] = board[(row, column + 1)] = board[(
                    row, column + 2)] = board[(row, column + 3)] = WIN_SYMBOL
                return True
    return False


def vertical_win(board):
    for row in range(3):
        for column in range(7):  # Limited rows to avoid KeyError
            if board[(row, column)] == board[(row + 1, column)] == board[(
                    row + 2, column)] == board[(row + 3, column)] != EMPTY:
                board[(row, column)] = board[(row + 1, column)] = board[(
                    row + 2, column)] = board[(row + 3, column)] = WIN_SYMBOL
                return True
    return False


def diagonal_win(board):
    for row in range(3):
        for column in range(4):
            # diagonal up to the right
            if board[(row + 3,
                      column)] == board[(row + 2, column + 1)] == board[(
                          row + 1,
                          column + 2)] == board[(row, column + 3)] != EMPTY:
                board[(row + 3,
                       column)] = board[(row + 2, column + 1)] = board[(
                           row + 1,
                           column + 2)] = board[(row, column + 3)] = WIN_SYMBOL
                return True
            # diagonal down to the right
            elif board[(row, column)] == board[(row + 1, column + 1)] == board[
                (row + 2, column + 2)] == board[(row + 3,
                                                 column + 3)] != EMPTY:
                board[(row, column)] = board[(row + 1, column + 1)] = board[(
                    row + 2, column + 2)] = board[(row + 3,
                                                   column + 3)] = WIN_SYMBOL
                return True

    return False


def get_initials(name):
    initials = ""
    for name in name.upper().split():
        initials += name[0]
    if len(initials) <= 3:
        return initials
    else:
        return f"{initials[0]}{initials[-1]}"


def display_title(title):
    title = "|".join(title.upper())
    print(f"[{title}]".center(29))


board = create_board()


def play_game():
    clear()
    winner = ""
    display_title("connect four")

    print()
    num_players = ""
    while num_players not in [1, 2]:
        num_players = (
            int(input("\nSelect number of human players (1 or 2):  ")))
    player1 = input("Player 1, what is your name?  ")
    current_player = get_initials(player1)
    if num_players == 2:
        player2 = input("Player 2, what is your name?  ")
        waiting_player = get_initials(player2)
    if num_players == 2 and current_player == waiting_player:
        current_player = str(current_player[0] + "1")
        waiting_player = str(waiting_player[0] + "2")
    else:  # set up computer
        waiting_player = COMPUTER

    print()

    game_still_going = True
    while game_still_going:
        if current_player != COMPUTER:
            play_turn(current_player)
        else:
            computer_turn(board, current_player)
        if game_won(board) or board_full(board):
            clear()
            display_board(board)
        if game_won(board):
            winner = current_player
            print(f"Congratulations, {winner}. You won!")
            game_still_going = False
        elif board_full(board):
            print("You tied.")
            game_still_going = False

        current_player, waiting_player = waiting_player, current_player


play_game()

valid_response = ["yes", "y", "yeah", "no", "n", "nope"]
response = ""
while not response in valid_response:
    response = input("\nWould you like to play again?: ").lower().strip()
    if response in ["yes", "y", "yeah"]:
        board = create_board()
        play_game()
    else:
        print("\nThanks for playing.")
        break

def reset_game():
    clear()
    board = create_board()
    display_board(board)
    print("reset game")
    return