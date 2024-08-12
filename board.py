import utilities
import constants


def display_board(board):
    labels = []
    for row in range(6):
        for column in range(7):
            labels.append(str(board[(row, column)]).center(3))
    utilities.display_title("connect four")
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


def board_full(board):
    for row in range(6):
        for column in range(7):
            if board[(row, column)] == constants.EMPTY:
                return False
    return True


def create_board():
    board = {}
    for row in range(6):
        for column in range(7):
            board[(row, column)] = constants.EMPTY
    return board