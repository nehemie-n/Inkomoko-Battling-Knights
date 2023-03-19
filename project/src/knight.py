import enum
from .item import Item, ITEM_NAME


class KNIGHT_STATUS(enum.Enum):
    LIVE = 1,
    DEAD = 2
    DROWNED = 3


class KNIGHT_COLOR(enum.Enum):
    R = "red"
    B = "blue"
    G = "green"
    Y = "yellow"

# colors = [KNIGHT_COLOR.__members__.get(color_str) for color_str in ["RED"]]
# print(colors)


class Knight:
    def __init__(self, color: KNIGHT_COLOR, position: tuple[int, int]):
        self.color: KNIGHT_COLOR = color
        self.position: tuple[int, int] = position
        self.status: KNIGHT_STATUS = KNIGHT_STATUS.LIVE
        self.item: Item = None
        self.attack: int = 1
        self.defense: int = 1

    def __str__(self):
        return f"{self.color} {self.status} {self.item} {self.attack} {self.defense}"

    def equip_item(self, item: Item):
        item.is_equiped = True
        self.item = item

    def remove_item(self):
        self.item.is_equiped = False
        self.item = None

    def is_alive(self):
        """Is the knight still alive"""
        return not self.status != KNIGHT_STATUS.LIVE

    def drawn(self):
        self.position = None
        self.status = KNIGHT_STATUS.DROWNED
        self.attack = 0
        self.defense = 0

    def dead(self):
        self.status = KNIGHT_STATUS.DEAD
        self.attack = 0
        self.defense = 0

    def change_position(self, position: tuple[int, int]):
        self.postion = position
