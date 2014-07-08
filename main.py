import blackjack

# TODO: handle non-integer inputs
def getPlayerBet(bank):
    bet = bank + 1

    while bet > bank:
        bet = int(input("Place your bet: "))

    return bet

def printDivider():
    print("#################################")

def printHand(hand):
    for card in hand:
        card.prettyPrint()
    print()

def printHidden(hand):
    hand[0].prettyPrint()
    print("|X|", sep="", end="")
    print()

def printGame(playerHand, dealerHand, hide):
    printDivider()
    print("Player: ")
    printHand(playerHand)
    print("Dealer: ")
    if hide:
        printHidden(dealerHand)
    else:
        printHand(dealerHand)
    printDivider()

def printBank(playerBank):
    print("Player Bank:", playerBank)

game = blackjack.Blackjack()

while True:
    print("Welcome to Blackjack!")
    playerBank = 100.0

    while playerBank > 0:
        printBank(playerBank)

        game.newGame()

        playerBet = getPlayerBet(playerBank)
        playerHand = []
        dealerHand = []

        game.deal(playerHand, dealerHand)

        printGame(playerHand, dealerHand, True)

        if blackjack.Blackjack.checkBlackjack(playerHand):
            print("BLACKJACK!")
            playerBank += blackjack.Blackjack.payBlackjack(playerBet)
        elif blackjack.Blackjack.checkBlackjack(dealerHand):
            print("Dealer Blackjack!")
            printGame(playerHand, dealerHand, False)
            playerBank -= playerBet
        else:
            while (not blackjack.Blackjack.isBusted(playerHand)):
                action = input("Hit (H) or Stand (S)?: ").upper()

                if action == 'S':
                    break
                elif action == 'H':
                    game.hit(playerHand)
                else:
                    print("Only H and S are valid commands.")

                printGame(playerHand, dealerHand, True)

            if blackjack.Blackjack.isBusted(playerHand):
                print("BUSTED!")
                playerBank -= playerBet
            else:
                while(blackjack.Blackjack.evaluateHand(dealerHand) < 17):
                    game.hit(dealerHand)
                    printGame(playerHand, dealerHand, False)
                    
                dealerScore = blackjack.Blackjack.evaluateHand(dealerHand)
                playerScore = blackjack.Blackjack.evaluateHand(playerHand)

                if blackjack.Blackjack.isBusted(dealerHand):
                    playerBank += playerBet
                    print("DEALER BUSTED!")
                elif dealerScore > playerScore:
                    playerBank -= playerBet
                    print("DEALER WINS!")
                elif dealerScore < playerScore:
                    playerBank += playerBet
                    print("PLAYER WINS!")
                else:
                    print("PUSH!")

    print("You lost all your money!")
    printDivider()
