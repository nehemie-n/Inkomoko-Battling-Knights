from .item import Item
from .knight import Knight


class Board:

    def __init__(self):
        # Define the initial state of the board
        self.__board = [[{"knight": None, "items": []}
                         for _ in range(8)] for _ in range(8)]

    def set_item(self, x: int, y: int, item: Item):
        self.__board[x][y]["items"].append(item)

    def remove_item(self, x: int, y: int, item: Item):
        self.__board[x][y]["items"].remove(item)

    def set_knight(self, x: int, y: int, knight: Knight):
        self.__board[x][y]["knight"] = knight

    def remove_knight(self, x: int, y: int):
        self.__board[x][y]["knight"] = None

    def has_knight(self, x: int, y: int):
        return self.__board[x][y]["knight"] is not None
    
    def get_knight(self, x: int, y: int):
        return self.__board[x][y]["knight"]

    def has_items(self, x: int, y: int):
        return len(self.__board[x][y]["items"]) > 0
    
    def pick_item(self,  x: int, y: int): 
        self.__board[x][y]["items"] = sorted(self.__board[x][y]["items"], key='order')
        return self.__board[x][y]["items"].pop()