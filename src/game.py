from knight import Knight, KNIGHT_COLOR
from item import Item, ITEM_NAME
import enum
import json


class DIRECTION(enum.Enum):
    N = "UP"
    E = "RIGHT"
    S = "DOWN"
    W = "LEFT"


class Game:
    moved = False

    def __init__(self):

        # Define the initial state of the board
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

        # Assign initial knights positions
        self.knights = {
            "R": Knight(KNIGHT_COLOR.R, (0, 0)),
            "B": Knight(KNIGHT_COLOR.B, (7, 0)),
            "G": Knight(KNIGHT_COLOR.G, (7, 7)),
            "Y": Knight(KNIGHT_COLOR.Y, (0, 7)),
        }
        self.board[0][0] = self.knights["R"]
        self.board[7][0] = self.knights["B"]
        self.board[7][7] = self.knights["G"]
        self.board[0][7] = self.knights["Y"]

        # assign initial items positions
        self.items = {
            "A": Item(ITEM_NAME.A, attack=2, position=(2, 2)),
            "D": Item(ITEM_NAME.D, attack=1, position=(2, 5)),
            "M": Item(ITEM_NAME.M, attack=1, defense=1, position=(5, 2)),
            "H": Item(ITEM_NAME.H, defense=1, position=(5, 5)),
        }
        self.board[2][2] = self.items["A"]
        self.board[2][5] = self.items["D"]
        self.board[5][2] = self.items["M"]
        self.board[5][5] = self.items["H"]

        self.moves = self.parse_moves()

    def parse_moves(self):
        """
        Parse the input file
        Add moves knight moves to the list and return it 
        """
        moves: list[tuple[Knight, DIRECTION]] = []
        with open('moves.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line == 'GAME-START':
                    continue
                elif line == 'GAME-END':
                    break
                else:
                    knight, direction = line.split(':')
                    knight = self.knights[knight]
                    direction = DIRECTION.__members__.get(direction)
                    moves.append((knight, direction))  # Add
        return moves

    def make_moves(self):
        """
        Make the game moves
        """
        if not self.moved:
            for move in self.moves:
                print(move)
                self.move_knight(knight=move[0], direction=move[1])
        self.moved = True

    def output_state(self):
        if not self.moved:
            raise Exception("You haven't made moves yet!")
        state = {}
        for knight in self.knights.values():
            state[str(knight.color._value_)] = [
                str(list(knight.position)),
                knight.status._name_,
                knight.item,
                knight.attack,
                knight.defense
            ]
        for item in self.items.values():
            state[str(item.name._value_)] = [
                str(list(item.position)),
                item.is_equiped,
            ]
        with open('final_state.json', 'w') as f:
            json.dump(state, f)
