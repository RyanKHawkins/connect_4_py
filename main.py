# Title:  Connect Four
# Author:  Ryan Hawkins
# Update:  2019-11-04

import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


EMPTY = "   "

# BOARD_WIDTH = 6
# BOARD_HEIGHT = 7


def create_board():
    board = {}
    for row in range(6):
        for column in range(7):
            board[(row, column)] = EMPTY
    return board


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
        while column_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            column_choice = input("Choose from 1 to 7: ")

        column = int(column_choice) - 1
        if board[(0, column)] == EMPTY:
            valid_choice = True
        else:
            valid_choice = False
            column_choice = input("That column is full. Choose another one: ")

    drop_piece(player, column)
    #display_board(board)


def column_full(column):
    if board[(0, column)] == EMPTY:
        return False
    return True


def board_full(board):
    for row in range(6):
        for column in range(7):
            if board[(row, column)] == EMPTY:
                return False
    print("Tie game.")
    return True


def drop_piece(player, column):
    row = 6
    placed = False
    while not placed:
        row -= 1
        if board[(row, column)] == EMPTY:
            board[(row, column)] = player
            placed = True


def check_for_win(board):
    horizontal_win(board)
    check_verticals(board)
    check_diagonals(board)


def horizontal_win(board):
    pass


def check_verticals(board):
    pass


def check_diagonals(board):
    pass


def get_initials():
    name = input("\nWhat is your name?\n")
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

    display_title("connect four")
    game_still_going = True

    current_player = get_initials()
    waiting_player = get_initials()
    print()

    while game_still_going:
        play_turn(current_player)
        check_for_win(board)
        if board_full(board):
            game_still_going = False
            #break

        current_player, waiting_player = waiting_player, current_player


play_game()

game_play = input("\nWould you like to play again?: ").lower().strip()
if game_play in ["yes", "y", "yeah"]:
    board = create_board()
    play_game()
else:
    print("Thanks for playing.")
