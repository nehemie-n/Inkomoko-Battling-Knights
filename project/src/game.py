from .item import Item, ITEM_NAME
from .move import DIRECTION
from .board import Board
import json
from .knight import Knight, Knight, KNIGHT_STATUS, KNIGHT_COLOR


class Game:
    moved = False

    def __init__(self, file_path="moves.txt"):
        self.file_path = file_path
        self.board = Board()
        # Assign initial knights positions
        self.knights = {
            "R": Knight(KNIGHT_COLOR.R, (0, 0)),
            "B": Knight(KNIGHT_COLOR.B, (7, 0)),
            "G": Knight(KNIGHT_COLOR.G, (7, 7)),
            "Y": Knight(KNIGHT_COLOR.Y, (0, 7)),
        }
        self.board.set_knight(x=0, y=0, knight=self.knights["R"])
        self.board.set_knight(x=7, y=0, knight=self.knights["B"])
        self.board.set_knight(x=7, y=7, knight=self.knights["G"])
        self.board.set_knight(x=0, y=7, knight=self.knights["Y"])

        # assign initial items positions
        self.items = {
            "A": Item(ITEM_NAME.A, attack=2, position=(2, 2)),
            "D": Item(ITEM_NAME.D, attack=1, position=(2, 5)),
            "M": Item(ITEM_NAME.M, attack=1, defense=1, position=(5, 2)),
            "H": Item(ITEM_NAME.H, defense=1, position=(5, 5)),
        }
        self.board.set_item(x=2, y=2, item=self.items["A"])
        self.board.set_item(x=2, y=5, item=self.items["D"])
        self.board.set_item(x=5, y=2, item=self.items["M"])
        self.board.set_item(x=5, y=5, item=self.items["H"])

    def play(self):
        """
        To ease testing
        """
        self.moves = self.__parse_moves()
        self.moves = self.__make_moves()
        self.moves = self.__output_state()

    def __parse_moves(self):
        """
        Parse the input file
        Add moves knight moves to the list and return it 
        """
        moves: list[tuple[Knight, DIRECTION]] = []
        with open(self.file_path, 'r') as f:
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

    def __make_moves(self):
        """
        Make the game moves
        """
        if not self.moved:
            for move in self.moves:
                print(move)
                self.__move_knight(knight=move[0], direction=move[1])
        self.moved = True

    def __move_knight(self, knight: Knight, direction):
        """
        Move a certain knight into a certain direction
        """
        print("MOVED __move_knight")
        if (knight.is_alive()):
            print("MOVED ALIVE __move_knight")
            """Move the knight in a certain direction provided"""
            px, py = knight.position
            x, y = knight.position
            # Baord
            self.board.remove_knight(x, y)  # Remove knight from prev position
            if (knight.item):
                # Remove item from prev position
                self.board.remove_item(x, y, knight.item)

            # Make moves
            if direction == DIRECTION.N:
                x -= 1
            elif direction == DIRECTION.S:
                x += 1
            elif direction == DIRECTION.E:
                y += 1
            elif direction == DIRECTION.W:
                y -= 1

            print("MOVED POSITION ", x, " ", y)
            # if drawned
            if not (0 <= x <= 7 and 0 <= y <= 7):
                if (knight.item):
                    # item stays in the position before drawn
                    knight.item.position = knight.position
                    knight.remove_item()
                knight.drawn()

            # if new position is perfect
            # @todo refactor, move codes the codes where a knight has an element in the knight class
            else:
                knight.change_position((x, y))

                if (knight.item):  # if had an item
                    knight.item.position = knight.position

                # if the board has an item here pick it
                if self.board.has_items(x, y):
                    if (knight.item is None):  # if we didn't have item before pick one
                        knight.equip_item(self.board.pick_item(x, y))

                # if this position has a knight before
                if self.board.has_knight(x, y):
                    print("HAS KNIGHT ", self.board.get_knight(x, y))
                    defender: Knight = self.board.get_knight(x, y)
                    won = self.__fight(attacker=knight, defender=defender)

                    if won:
                        defender.dead()
                        if (defender.item):  # if had an item
                            defender.item.position = (x, y)
                            defender.remove_item()
                        self.board.set_knight(x, y, knight)
                    else:
                        knight.dead()
                        if (knight.item):  # if had an item
                            knight.item.position = (x, y)
                            knight.remove_item()

                else:
                    # In the end update the board with new
                    self.board.set_knight(x, y, knight=knight)

    def __fight(self, attacker: Knight, defender: Knight):
        """Fighting for knights"""
        if defender.status == KNIGHT_STATUS.LIVE:
            # Attack score
            attacker_score = attacker.attack + 0.5  # element of surprise
            attacker_score = attacker_score + \
                attacker.item.attack if attacker.item is not None else attacker_score
            # defense score
            defender_score = defender.defense + \
                defender.item.defense if defender.item is not None else defender.defense
            #
            if attacker_score > defender_score:
                return True
            else:
                return False

    def __output_state(self):
        """
        Dumps the output in the .json file
        """
        if not self.moved:
            raise Exception("You haven't made moves yet!")
        self.state = {}
        for knight in self.knights.values():
            self.state[str(knight.color._value_)] = [
                str(list(knight.position)) if knight.position else None,
                knight.status._name_,
                str(knight.item) if knight.item else None,
                knight.attack,
                knight.defense
            ]
        for item in self.items.values():
            self.state[str(item.name._value_)] = [
                str(list(item.position)),
                item.is_equiped,
            ]
        with open('final_state.json', 'w') as f:
            json.dump(self.state, f)
