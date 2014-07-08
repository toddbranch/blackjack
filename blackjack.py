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

    def __init__(self):
        self.gameDeck = deck.Deck()

    def newGame(self):
        self.gameDeck.shuffle()

    def deal(self, playerHand, dealerHand):
        for i in range(2):
            playerHand.append(self.gameDeck.deal())
            dealerHand.append(self.gameDeck.deal())

    def hit(self, hand):
        hand.append(self.gameDeck.deal())

    @classmethod
    def evaluateHand(cls, hand):
        handValue = 0

        for card in hand:
            handValue += cls.getCardValue

        return handValue

    @classmethod
    def getCardValue(cls, card):
        return cls._cardValues[card.value]

    @classmethod
    def checkBlackjack(cls, hand):
        if len(hand) > 2:
            return False

        if cls.evaluateHand(hand) == 21:
            return True

        return False

    @staticmethod
    def payBlackjack(bet):
        return bet * 3/2