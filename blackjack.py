import deck

class Blackjack:

    _cardValues = {
                    '2': 2,
                    '3': 3,
                    '4': 4,
                    '5': 5,
                    '6': 6,
                    '7': 7,
                    '8': 8,
                    '9': 9,
                    'T': 10,
                    'J': 10,
                    'Q': 10,
                    'K': 10,
                    'A': 11
            }

    def __init__(self, bankroll):
        self.gameDeck = deck.Deck()
        self.resetBankroll(bankroll)

    def newGame(self):
        self.gameDeck.shuffle()
        self.dealerHand = []
        self.playerHand = []

    def resetBankroll(self, bankroll):

    def printHands(self):

    def hitPlayer(self):
        self.playerHand.append(self.gameDeck.deal())

    def hitDealer(self):
        self.dealerHand.append(self.gameDeck.deal())

    def evaluateHand(self, hand):
        handValue = 0

        for card in hand:
            handValue += self.getCardValue

        if handValue <= 21:
            return handValue
        else:


    def getCardValue(self, card):
        return Blackjack._cardValues[card.value]
