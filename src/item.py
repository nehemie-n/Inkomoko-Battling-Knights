import enum
# Using enum class create enumerations


class Item:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.status = "LIVE"
        self.item = None
        self.attack = 1
        self.defense = 1
