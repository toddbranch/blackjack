# blackjack

To run: `python main.py`

Tested using Python 3.4.1

Written for insight data fellows program.  Would love to refactor more and add split, but am leaving for vacation tomorrow morning!

## General

- Player starts with 100 chips
- Bets between 1 and the amount of chips the player has are allowable
- Allowable actions for the player:
  - (H)it 
    - player is dealt one additional card
    - if the player doesn't bust, they can take additional action(s)
  - (S)tand
    - player is dealt no additional cards
    - player can take no additional action(s)
  - (D)ouble
    - player doubles bet
    - player is dealt one additional card
    - player can take no additional action(s)
- Dealer must hit until their hand totals at least 17, then cannot hit
- Dealer **does not** hit soft 17
- Game Outcomes:
  - **Push**: the player and dealer tie - the bet is returned to the player
  - **Dealer Wins**: dealer has more than player and less than 21 - bet is forfeited by the player
  - **Player Wins**: player has more than dealer and less than 21 - player is paid their bet
  - **Dealer Bust**: dealer has more than 21 - player is paid their bet
  - **Player Bust**: player has more than 21 - bet is foreited by the player
  - **Player Blackjack**: player is dealt 21 (first two cards) - player is paid 1.5 times their bet
  - **Dealer Blackjack**: dealer is dealt 21 (first two cards) - bet is forfeited by player

## Classes

### Card

Simple class to represent a card.

- Attributes:
  - `value`
  - `suit`
- Methods:
  - `__init__` - creates card with given value and suit
  - `prettyPrint` - print value of card between vertical bars

### Deck

Class to represent a deck.

- Attributes:
  - `sequence` - array containing deck cards in order
  - `discard` - array containing cards previously dealt
- Methods:
  - `__init__` - generates full deck in order
  - `shuffle` - implements Fisher-Yates shuffle
  - `swap` - swaps cards to support shuffle
  - `deal` - pops card off deck, adds to discard, returns to caller
  - `printDeck` - prints the current sequence of cards to console

### Blackjack

Class to encapsulate common game functions to allow main to focus on data input/output.

- Attributes:
  - `gameDeck` - Deck instance holding current deck
  - `playerHand` - array that holds player cards
  - `dealerHand` - array that holds dealer cards
- Methods:
  - `__init__` - initializes `gameDeck`
  - `newGame` - shuffles `gameDeck`, initializes `playerHand` and `dealerHand`
  - `deal` - deals 2 cards to player and dealer by alternating
  - `hitPlayer` - deals card to player
  - `hitDealer` - deals card to dealer
  - `isPlayerBusted` - returns True if hand is over 21
  - `isDealerBusted` - returns True if hand is over 21
  - `isDealerComplete` - returns True if dealer hand is over 16
  - `didPlayerBlackjack` - returns True if first two cards total 21
  - `didDealerBlackjack` - returns True if first two cards total 21
  - `handResult` - evaluates hands, returns "dealer win", "player win", or "push" depending on result
  - `printGame` - prints hands of player and dealer to console
  - `evaluateHand` - `classmethod` - returns numeric value of hand
  - `getCardValue` - `classmethod` - returns numberic value of card
  - `checkBlackjack` - `classmethod` - checks whether hand is blackjack
  - `isBusted` - `classmethod` - checks whether hand is over 21
  - `payBlackjack` - `staticmethod` - returns 3/2 * bet
  - `payWin` - `staticmethod` - returns bet
  - `printHand` - `staticmethod` - prints each card in hand
  - `printHidden` - `staticmethod` - prints the second dealer card as X to hide it

## main

Handles input / output for general gameplay.  Manages general gameplay and player bank using an instance of `Blackjack`.
