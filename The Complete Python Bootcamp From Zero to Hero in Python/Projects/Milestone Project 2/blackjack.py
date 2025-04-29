import random

"""
Declared variables to store suits, ranks and values.
Declared a Boolean value to be used to control while loops.
"""
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    """
    Made a Card class where each Card object has a suit and a rank.
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        When asked to print a Card, returns a string in the form example: "Two of Hearts"
        """
        return self.rank + ' of ' + self.suit


class Deck:
    """
    Made a Deck class to hold all 52 Card objects, and can be shuffled.
    """

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        """
        When asked to print a Deck, returns strings of all 52 cards.
        """
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    """
    Made a Hand class that holds those Cards, that have been dealt to each player from the Deck.
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Is used to calculate the value of those cards using the values dictionary.
        """
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        """
        Adjusts for the value of Aces when appropriate.
        """
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    """
    Made a Chips class that keeps track of a Player's starting chips, bets, and ongoing winnings.
    """

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    """
    Asks the user for an integer value.
    Checks if a Player's bet can be covered by their available chips.
    If it can't be covered, it breaks from the while loop.
    """
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Please provide an integer.')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have:', chips.total)
            else:
                break


def hit(deck, hand):
    """
    Is called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17.
    It takes in Deck and Hand objects as arguments, and deals one card off the deck and adds it to the Hand.
    Either player takes hits until they bust.
    """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """
    Accepts the deck and the player's hand as arguments, and assigns playing as a global variable.
    """
    global playing

    while True:
        """
        if the Player Hits, employs the hit() function above. If the Player Stands, sets the playing variable to False.
        """
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print('Sorry, I did not understand that, Please enter h or s only!')
            continue
        break


def show_some(player, dealer):
    """
    Shows each hand's cards.
    All the cards of the Player are visible, but the Dealer's first card is always hidden at the beginning.
    """
    print("\n Dealer's Hand: ")
    print('First card hidden!')
    print(dealer.cards[1])

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    """
    Shows each hand's total value.
    """
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player, dealer, chips):
    """
    Handles end of game scenarios.
    """
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    """
    Handles end of game scenarios.
    """
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    """
    Handles end of game scenarios.
    """
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    """
    Handles end of game scenarios.
    """
    print('DEALER WINS!')
    chips.lose_bet()


def push(player, dealer):
    """
    Handles end of game scenarios.
    """
    print('Dealer and Player Tie! PUSH!')


def run_game():
    """
    Uses while loops and the functions made to run the game!
    """
    global playing
    print('WELCOME TO BLACKJACK!')
    while True:
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()

        take_bet(player_chips)

        show_some(player_hand, dealer_hand)

        while playing:
            hit_or_stand(deck, player_hand)

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print(f'\n Player total chips are: {player_chips.total}')

        while True:
            new_game = input("Would you like to play again? y/n ")
            if new_game[0].lower() == 'y':
                playing = True
                break
            elif new_game[0].lower() == 'n':
                print('Thank you for playing!')
                return
            else:
                print('Invalid input. Please enter y or n!')


if __name__ == "__main__":
    run_game()
