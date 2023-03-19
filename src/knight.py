import enum
from item import Item, ITEM_NAME


class KNIGHT_STATUS(enum.Enum):
    LIVE = 1,
    DEAD = 2
    DROWNED = 3


class KNIGHT_COLOR(enum.Enum):
    R = "red"
    B = "blue"
    G = "green"
    Y = "Yellow"

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
        self.item = item

    def remove_item(self):
        self.item = None

    def fight(self, defender):
        if defender.status == KNIGHT_STATUS.LIVE:
            # Attack score
            attacker_score = self.attack + 0.5
            attacker_score = attacker_score + \
                self.item.attack if self.item is not None else attacker_score
            # defense score
            defender_score = defender.defense + \
                defender.item.defense if defender.item is not None else defender.defense
            #
            if attacker_score > defender_score:
                defender.status = KNIGHT_STATUS.DEAD
                defender.remove_item()
                return True
            else:
                self.status = KNIGHT_STATUS.DEAD
                self.remove_item()
                return False

    def is_alive(self):
        pass
