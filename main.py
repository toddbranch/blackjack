import blackjack

def getPlayerBet(bank):
    bet = bank + 1

    while bet > bank:
        bet = input("Place your bet: ")

    return bet

game = blackjack.Blackjack()

while True:
    print "Welcome to Blackjack!"
    playerBank = 100

    while playerBank > 0:
        game.newGame()

        playerBet = getPlayerBet(playerBank)
        playerHand = []
        dealerHand = []

        game.deal(playerHand, dealerHand)
