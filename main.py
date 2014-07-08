from blackjack import Blackjack

#TODO: Refactor - a lot of this should be moved into the blackjack module, main.py should be primarily for handling user input

# TODO: handle non-integer inputs
def getPlayerBet(bank):
    bet = bank + 1

    while bet > bank:
        try:
            bet = int(input("Place your bet: "))
        except ValueError:
            print("Bets must be a numeric value!")
            printDivider()

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
    printDivider()

game = Blackjack()

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

        if Blackjack.checkBlackjack(playerHand):
            print("BLACKJACK!")
            playerBank += Blackjack.payBlackjack(playerBet)
        elif Blackjack.checkBlackjack(dealerHand):
            print("Dealer Blackjack!")
            printGame(playerHand, dealerHand, False)
            playerBank -= playerBet
        else:
            while (not Blackjack.isBusted(playerHand)):
                action = input("Hit (H) or Stand (S)?: ").upper()

                if action == 'S':
                    break
                elif action == 'H':
                    game.hit(playerHand)
                else:
                    print("Only H and S are valid commands.")

                printGame(playerHand, dealerHand, True)

            if Blackjack.isBusted(playerHand):
                print("BUSTED!")
                playerBank -= playerBet
            else:
                printGame(playerHand, dealerHand, False)

                while(Blackjack.evaluateHand(dealerHand) < 17):
                    game.hit(dealerHand)
                    printGame(playerHand, dealerHand, False)
                    
                dealerScore = Blackjack.evaluateHand(dealerHand)
                playerScore = Blackjack.evaluateHand(playerHand)

                if Blackjack.isBusted(dealerHand):
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
