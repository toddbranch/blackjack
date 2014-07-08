from blackjack import Blackjack

################################################################
# Helper Functions
################################################################

def getPlayerBet(bank):
    bet = bank + 1

    while bet > bank:
        try:
            bet = float(input("Place your bet: "))
        except ValueError:
            print("Bets must be a numeric value!")
            printDivider()

    return bet

def getPlayerAction():
    action = ""
    while action != 'S' and action != 'H':
        print("Only (H)it and (S)tand are valid commands.")
        action = input("(H)it or (S)tand?: ").upper()

    return action

def printGameDealerHidden(game):
    printDivider()
    game.printGame(True)
    printDivider()

def printGameDealerVisible(game):
    printDivider()
    game.printGame(False)
    printDivider()

def printDivider():
    print("###########################################")

def printBank(playerBank):
    print("Player Bank:", playerBank)
    printDivider()

def gameOver():
    print("You lost all your money!")
    print("Restarting game...")
    printDivider()

def push(bank, bet):
    print("PUSH")
    return bank

def dealer_win(bank, bet):
    print("DEALER WINS!")
    return bank - bet

def player_win(bank, bet):
    print("PLAYER WINS!")
    return bank + Blackjack.payWin(bet)

game_results = {
                    "player_win": player_win,
                    "dealer_win": dealer_win,
                    "push": push
        }

def playerBlackjack(bank, bet):
    print("BLACKJACK!")
    return bank + Blackjack.payBlackjack(bet)

def dealerBlackjack(bank, bet):
    print("Dealer Blackjack!")
    return bank - bet

def dealerBusted(bank, bet):
    print("DEALER BUSTED!")
    return bank + bet

def playerBusted(bank, bet):
    print("PLAYER BUSTED!")
    return bank - bet

################################################################
# Game logic
################################################################

game = Blackjack()

while True:

    ############################################################
    # Reset game
    ############################################################

    print("Welcome to Blackjack!")
    playerBank = 100.0

    while playerBank > 0:

        ########################################################
        # Play next hand
        ########################################################

        printBank(playerBank)

        game.newGame()

        playerBet = getPlayerBet(playerBank)

        game.deal()

        printGameDealerHidden(game)

        if game.didPlayerBlackjack():
            playerBank = playerBlackjack(playerBank, playerBet)
        elif game.didDealerBlackjack():
            printGameDealerVisible(game)
            playerBank = dealerBlackjack(playerBank, playerBet)
        else:
            while not game.isPlayerBusted():
                action = getPlayerAction()

                if action == 'S':
                    break
                else:
                    game.hitPlayer()

                printGameDealerHidden(game)

            if game.isPlayerBusted():
                playerBank = playerBusted(playerBank, playerBet)
            else:
                printGameDealerVisible(game)

                while not game.isDealerComplete():
                    game.hitDealer()
                    printGameDealerVisible(game)
                    
                if game.isDealerBusted():
                    playerBank = dealerBusted(playerBank, playerBet)
                else:
                    playerBank = game_results[game.handResult()](playerBank, playerBet)            

    gameOver()
