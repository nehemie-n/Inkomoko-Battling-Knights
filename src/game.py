from .knight import Knight, KNIGHT_COLOR
from .item import Item, ITEM_NAME
import enum


class MOVE(enum.Enum):
    N = "UP"
    E = "RIGHT"
    S = "DOWN"
    W = "LEFT"


class Game:
    def __init__(self):

        # Define the initial state of the board
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

        # Assign initial knights positions
        self.board[0][0] = Knight(KNIGHT_COLOR.RED, (0, 0))
        self.board[7][0] = Knight(KNIGHT_COLOR.BLUE, (7, 0))
        self.board[7][7] = Knight(KNIGHT_COLOR.GREEN, (7, 7))
        self.board[0][7] = Knight(KNIGHT_COLOR.YELLOW, (0, 7))

        # assign initial items positions
        self.board[2, 2] = Item(ITEM_NAME.A, attack_bonus=2)
        self.board[2, 5] = Item(ITEM_NAME.D, attack_bonus=1)
        self.board[5, 2] = Item(ITEM_NAME.M, attack_bonus=1, defence_bonus=1)
        self.board[5, 5] = Item(ITEM_NAME.H, defence_bonus=1)
