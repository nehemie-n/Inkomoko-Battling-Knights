import enum
from .item import Item


class KNIGHT_STATUS(enum.Enum):
    LIVE = 1,
    DEAD = 2
    DROWNED = 3


class KNIGHT_COLOR(enum.Enum):
    R = "RED"
    B = "BLUE"
    G = "GREEN"
    Y = "YELLOW"


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
        if item == "A":
            self.attack += 2
        elif item == "D":
            self.attack += 1
        elif item == "H":
            self.defense += 1
        elif item == "M":
            self.attack += 1
            self.defense += 1
        self.item = item

    def remove_item(self):
        if self.item == "A":
            self.attack -= 2
        elif self.item == "D":
            self.attack -= 1
        elif self.item in ["H", "M"]:
            self.defense -= 1
            if self.item == "M":
                self.attack -= 1
        self.item = None

    def fight(self, other):
        if other.status == KNIGHT_STATUS.LIVE:
            attacker_score = self.attack + 0.5 if self.item is not None else self.attack
            defender_score = other.defense + 0.5 if other.item is not None else other.defense
            if attacker_score > defender_score:
                other.status = KNIGHT_STATUS.DEAD
                other.remove_item()
                return True
            else:
                self.status = KNIGHT_STATUS.DEAD
                self.remove_item()
                return False
