class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def prettyPrint(self):
        return "|" + self.value + "|"
