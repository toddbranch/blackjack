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
                    'A': 1      # also 11, but default to 1
            }

    def __init__(self):
        self.gameDeck = deck.Deck()

    def newGame(self):
        self.gameDeck.shuffle()
        self.playerHand = []
        self.dealerHand = []

    def deal(self):
        for i in range(2):
            self.playerHand.append(self.gameDeck.deal())
            self.dealerHand.append(self.gameDeck.deal())

    def hitPlayer(self):
        self.playerHand.append(self.gameDeck.deal())

    def hitDealer(self):
        self.dealerHand.append(self.gameDeck.deal())

    def isPlayerBusted(self):
        return self.isBusted(self.playerHand)

    def isDealerBusted(self):
        return self.isBusted(self.dealerHand)

    def isDealerComplete(self):
        return self.evaluateHand(self.dealerHand) >= 17

    def didPlayerBlackjack(self):
        return self.checkBlackjack(self.playerHand)

    def didDealerBlackjack(self):
        return self.checkBlackjack(self.dealerHand)

    # API consumers must interpret the result strings returned
    # Using a dictionary with these strings as keys to functions works well
    def handResult(self):
        dealerScore = self.evaluateHand(self.dealerHand)
        playerScore = self.evaluateHand(self.playerHand)

        if dealerScore > playerScore:
            return "dealer_win"
        elif dealerScore < playerScore:
            return "player_win"
        else:
            return "push"

    def printGame(self, hideDealerCard):
        print("Player: ")
        self.printHand(self.playerHand)

        print("Dealer: ")
        if hideDealerCard:
            self.printHidden(self.dealerHand)
        else:
            self.printHand(self.dealerHand)

    @classmethod
    def evaluateHand(cls, hand):
        handValue = 0
        aces = 0

        for card in hand:
            handValue += cls.getCardValue(card)
            if card.value == "A":
                aces += 1

        if aces > 0:
            if handValue + 10 <= 21:
                return handValue + 10

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

    @classmethod
    def isBusted(cls, hand):
        if cls.evaluateHand(hand) > 21:
            return True
        else:
            return False

    @staticmethod
    def payBlackjack(bet):
        return bet * 3/2

    @staticmethod
    def payWin(bet):
        return bet


    @staticmethod
    def printHand(hand):
        for card in hand:
            print(card.prettyPrint(), end="")
        print()

    @staticmethod
    def printHidden(hand):
        print(hand[0].prettyPrint(), end="")
        print("|X|")
