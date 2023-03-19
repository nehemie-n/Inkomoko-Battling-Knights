import enum
# Using enum class create enumerations


class ITEM_NAME(enum.Enum):
    A = "axe"
    D = "dagger"
    H = "helmet"
    M = "magic stick"


class Item:
    def __init__(self, name: ITEM_NAME, position: tuple[int, int], attack=0, defense=0):
        self.name = name
        self.attack: int = attack
        self.defense: int = defense
        self.is_equiped: bool = False
        self.position: tuple[int, int] = position

    def __repr__(self):
        return f"{self.name} ({self.attack=}, {self.defense=})"

    def apply_bonus(self, attack, defense):
        self.attack += attack
        self.defense += defense

    def iis(self, name: ITEM_NAME):
        return self.name == name

    def change_position(self, position: tuple[int, int]):
        self.postion = position
