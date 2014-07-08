from blackjack import Blackjack

################################################################
# Helper Functions
################################################################

def getPlayerBet(bank):
    bet = 0

    while bet > bank or bet < 1.0:
        try:
            print("Bets must be more than 1 and less than Player Bank.")
            bet = float(input("Place your bet: "))
        except ValueError:
            print("Bets must be a numeric value!")
            printDivider()

    return bet

actions = ['S', 'H', 'D']

# TODO: Double-down logic can be added here
def getPlayerAction():
    action = ""
    while action not in actions:
        print("Only (H)it, (S)tand, or (D)ouble are valid commands.")
        action = input("(H)it, (S)tand, or (D)ouble?: ").upper()

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
    print("######################################################")

def printBank(playerBank):
    print("Player Bank:", playerBank)
    printDivider()

def gameOver():
    print("YOU LOST ALL YOUR MONEY!")
    print("Restarting game...")
    printDivider()

def push(bank, bet):
    print("PUSH!")
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
    print("DEALER BLACKJACK!")
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
            # TODO: Split logic goes here

            while not game.isPlayerBusted():
                action = getPlayerAction()

                if action == 'S':
                    break
                elif action == 'D':
                    if playerBank >= playerBet * 2:
                        playerBet += playerBet
                        game.hitPlayer()
                        printGameDealerHidden(game)
                        break
                    else:
                        print("You don't have enough chips to make that bet!")
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
