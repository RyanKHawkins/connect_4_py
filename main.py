# Title:  Connect Four
# Author:  Ryan Hawkins

import random
import os
import time
import utilities
import board
import constants


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_turn(player):
    clear()
    board.display_board(current_board)
    column_choice = input(f"Player {player}, place your piece (1-7): ")
    valid_choice = False
    while not valid_choice:
        while column_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            column_choice = input("Choose from 1 to 7: ")

        column = int(column_choice) - 1
        
        if current_board[(0, column)] == constants.EMPTY:
            valid_choice = True
        else:
            valid_choice = False
            column_choice = input("That column is full. Choose another one: ")

    drop_piece(player, column)
    board.display_board(current_board)


def computer_turn(current_board, player):
    # computer randomly chooses from available columns
    available_columns = []
    time.sleep(.5)
    for column in range(7):
        if current_board[(0, column)] == constants.EMPTY:
            available_columns.append(column)
    column_choice = random.choice(available_columns)
    drop_piece(player, column_choice)


def column_full(column):
    if current_board[(0, column)] == constants.EMPTY:
        return False
    return True


def drop_piece(player, column):
    row = 6
    placed = False
    while not placed:
        row -= 1
        if current_board[(row, column)] == constants.EMPTY:
            current_board[(row, column)] = player
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
                    row, column + 2)] == board[(row, column + 3)] != constants.EMPTY:
                board[(row, column)] = board[(row, column + 1)] = board[(
                    row, column + 2)] = board[(row, column + 3)] = constants.WIN_SYMBOL
                return True
    return False


def vertical_win(board):
    for row in range(3):
        for column in range(7):  # Limited rows to avoid KeyError
            if board[(row, column)] == board[(row + 1, column)] == board[(
                    row + 2, column)] == board[(row + 3, column)] != constants.EMPTY:
                board[(row, column)] = board[(row + 1, column)] = board[(
                    row + 2, column)] = board[(row + 3, column)] = constants.WIN_SYMBOL
                return True
    return False


def diagonal_win(board):
    for row in range(3):
        for column in range(4):
            # diagonal up to the right
            if board[(row + 3,
                      column)] == board[(row + 2, column + 1)] == board[(
                          row + 1,
                          column + 2)] == board[(row, column + 3)] != constants.EMPTY:
                board[(row + 3,
                       column)] = board[(row + 2, column + 1)] = board[(
                           row + 1,
                           column + 2)] = board[(row, column + 3)] = constants.WIN_SYMBOL
                return True
            # diagonal down to the right
            elif board[(row, column)] == board[(row + 1, column + 1)] == board[
                (row + 2, column + 2)] == board[(row + 3,
                                                 column + 3)] != constants.EMPTY:
                board[(row, column)] = board[(row + 1, column + 1)] = board[(
                    row + 2, column + 2)] = board[(row + 3,
                                                   column + 3)] = constants.WIN_SYMBOL
                return True

    return False


def play_game():
    clear()
    winner = ""
    utilities.display_title("connect four")

    print()
    num_players = ""
    while num_players not in ["1", "2"]:
        num_players = (
            input("\nSelect number of human players (1 or 2):  "))
    player1 = input("Player 1, what is your name?  ")
    current_player = utilities.get_initials(player1)
    if num_players == 2:
        player2 = input("Player 2, what is your name?  ")
        waiting_player = utilities.get_initials(player2)
    if num_players == 2 and current_player == waiting_player:
        current_player = str(current_player[0] + "1")
        waiting_player = str(waiting_player[0] + "2")
    else:  # set up computer
        waiting_player = constants.COMPUTER

    print()

    game_still_going = True
    while game_still_going:
        if current_player != constants.COMPUTER:
            play_turn(current_player)
        else:
            computer_turn(current_board, current_player)
        if game_won(current_board) or board.board_full(current_board):
            clear()
            board.display_board(current_board)
        if game_won(current_board):
            winner = current_player
            print(f"Congratulations, {winner}. You won!")
            game_still_going = False
        elif board.board_full(current_board):
            print("You tied.")
            game_still_going = False

        current_player, waiting_player = waiting_player, current_player


playing = True
while playing == True:
    current_board = board.create_board()
    play_game()
    valid_responses = ["yes", "y", "yeah", "no", "n", "nope"]
    response = ""
    while not response in valid_responses:
        response = input("\nWould you like play again? ")
        response = response.lower().strip()
        if response in ["no", "n", "nope"]:
            playing = False

