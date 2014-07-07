import card
import random

class Deck:
    deckSize = 52
    suits = ["D", "H", "S", "C"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self):
        random.seed()

        self.sequence = []
        self.discard = []

        for suit in Deck.suits:
            for value in Deck.values:
                self.sequence.append(card.Card(value, suit))

    # Fisher-Yates shuffle
    def shuffle(self):
        self.sequence += self.discard
        self.discard = []

        for i in range(Deck.deckSize-1,0,-1):
            self.swap(i, random.randrange(i))

    def swap(self, index1, index2):
       temp = self.sequence[index2]
       self.sequence[index2] = self.sequence[index1]
       self.sequence[index1] = temp
    
    def deal(self):
        dealtCard = self.sequence.pop()
        self.discard.append(dealtCard)
        
        return dealtCard

    def printDeck(self):
        for element in self.sequence:
            element.prettyPrint()
