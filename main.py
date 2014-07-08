import blackjack

# TODO: handle non-integer inputs
def getPlayerBet(bank):
    bet = bank + 1

    while bet > bank:
        bet = int(input("Place your bet: "))

    return bet

def printDivider():
    print("#################################")

def printGame(playerHand, dealerHand):
    printDivider()
    print("Player: ")
    for card in playerHand:
        card.prettyPrint()
    print()
    print("Dealer: ")
    for card in dealerHand:
        card.prettyPrint()
    print()
    printDivider()

def printBank(playerBank):
    print("Player Bank:", playerBank)

game = blackjack.Blackjack()

while True:
    print("Welcome to Blackjack!")
    playerBank = 100

    while playerBank > 0:
        printBank(playerBank)

        game.newGame()

        playerBet = getPlayerBet(playerBank)
        playerHand = []
        dealerHand = []

        game.deal(playerHand, dealerHand)

        printGame(playerHand, dealerHand)

        if blackjack.Blackjack.checkBlackjack(playerHand):
            print("BLACKJACK!")
            playerBank += blackjack.Blackjack.payBlackjack(playerBet)
        elif blackjack.Blackjack.checkBlackjack(dealerHand):
            print("Dealer Blackjack!")
            playerBank -= playerBet
        else:
            while (not blackjack.Blackjack.isBusted(playerHand)):
                action = input("Hit (H) or Stand (S)?: ")

                if action == 'S':
                    break
                elif action == 'H':
                    game.hit(playerHand)
                else:
                    print("Only H and S are valid commands.")

                printGame(playerHand, dealerHand)

            if blackjack.Blackjack.isBusted(playerHand):
                print("BUSTED!")
                playerBank -= playerBet


    print("You lost all your money!")
    printDivider()
