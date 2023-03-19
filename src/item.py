import enum
# Using enum class create enumerations


class ITEM_NAME(enum.Enum):
    A = "Axe"
    D = "Dagger"
    H = "Helmet"
    M = "Magic Stick"


class Item:
    def __init__(self, name: ITEM_NAME, attack=0, defense=0):
        self.name = name
        self.attack: int = attack
        self.defense: int = defense

    def __repr__(self):
        return f"{self.name} ({self.attack=}, {self.defense=})"

    def apply_bonus(self, attack, defense):
        self.attack += attack
        self.defense += defense

    def iis(self, name: ITEM_NAME):
        return self.name == name
