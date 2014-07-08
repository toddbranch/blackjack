class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def prettyPrint(self):
        print("|", self.value, "|", sep="", end="")
