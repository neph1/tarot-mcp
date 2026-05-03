class Card:

    def __init__(self, name: str, reversed: bool = False):
        self.name = name
        self.reversed = reversed

    def __str__(self):
        return self.name +  ' (Reversed)' if self.reversed else ''