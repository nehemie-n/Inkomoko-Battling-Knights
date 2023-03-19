import enum
# Using enum class create enumerations


class ITEM_NAME(enum.Enum):
    A = "Axe"
    D = "Dagger"
    H = "Helmet"
    M = "Magic Stick"


class Item:
    def __init__(self, name: ITEM_NAME, attack=0, defence=0):
        self.name = name
        self.attack: int = attack
        self.defence: int = defence

    def __repr__(self):
        return f"{self.name} ({self.attack=}, {self.defence=})"

    def apply_bonus(self, attack, defence):
        self.attack += attack
        self.defence += defence

    def iis(self, name: ITEM_NAME):
        return self.name == name
