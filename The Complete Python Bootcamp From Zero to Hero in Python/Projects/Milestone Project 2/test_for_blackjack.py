import unittest
from unittest.mock import patch
from io import StringIO
from blackjack import Card, Deck, Hand, Chips, hit, values


class TestCard(unittest.TestCase):
    def test_card_str(self):
        """Tests if the Card's string representation is correct."""
        card = Card('Hearts', 'Two')
        self.assertEqual(str(card), 'Two of Hearts')


class TestDeck(unittest.TestCase):
    def test_deck_has_52_cards(self):
        """Tests if a new deck contains exactly 52 cards."""
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)

    def test_deal_returns_card(self):
        """Tests if deal() removes and returns a Card object."""
        deck = Deck()
        card = deck.deal()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.deck), 51)

    def test_shuffle_changes_order(self):
        """Tests if shuffle() changes the order of cards in the deck."""
        deck = Deck()
        original_order = [str(card) for card in deck.deck]
        deck.shuffle()
        shuffled_order = [str(card) for card in deck.deck]
        self.assertNotEqual(original_order, shuffled_order)


class TestHand(unittest.TestCase):
    def test_add_card(self):
        """Tests if add_card() adds a card and updates hand value correctly."""
        hand = Hand()
        card = Card('Hearts', 'Two')
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.value, 2)

    def test_add_ace_and_adjust(self):
        """Tests adding an Ace and adjusting its value to avoid busting."""
        hand = Hand()
        hand.add_card(Card('Hearts', 'Ace'))  # 11
        hand.add_card(Card('Diamonds', 'King'))  # 10 → total 21
        self.assertEqual(hand.value, 21)

        hand.add_card(Card('Clubs', 'Five'))  # the total becomes 26
        hand.adjust_for_ace()
        self.assertEqual(hand.value, 16)  # Ace becomes 1


class TestChips(unittest.TestCase):
    def test_initial_total(self):
        """Tests if a new Chips object starts with 100 chips by default."""
        chips = Chips()
        self.assertEqual(chips.total, 100)

    def test_win_bet(self):
        """Tests if win_bet() adds the current bet to the total chips."""
        chips = Chips()
        chips.bet = 20
        chips.win_bet()
        self.assertEqual(chips.total, 120)

    def test_lose_bet(self):
        """Tests if lose_bet() subtracts the current bet from total chips."""
        chips = Chips()
        chips.bet = 30
        chips.lose_bet()
        self.assertEqual(chips.total, 70)


class TestHitFunction(unittest.TestCase):
    def test_hit_adds_card_and_adjusts_for_ace(self):
        """Tests if hit() deals a card and adjusts for ace correctly."""
        deck = Deck()
        deck.deck = [Card('Spades', 'Ace')]  # top card of the deck
        hand = Hand()
        hit(deck, hand)
        self.assertEqual(hand.value, 11)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.aces, 1)


class TestGameplayScenarios(unittest.TestCase):
    @patch('builtins.input', side_effect=['50'])
    def test_take_bet_valid_input(self, mock_input):
        """Tests if take_bet() correctly assigns a valid bet."""
        from blackjack import take_bet
        chips = Chips()
        with patch('sys.stdout', new=StringIO()):  # suppress output
            take_bet(chips)
        self.assertEqual(chips.bet, 50)

    @patch('builtins.input', side_effect=['abc', '200', '30'])
    def test_take_bet_invalid_then_valid(self, mock_input):
        """Tests take_bet() handles non-integer and over-limit bets before accepting a valid one."""
        from blackjack import take_bet
        chips = Chips()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            take_bet(chips)
            output = fake_out.getvalue()
        self.assertIn('Please provide an integer.', output)
        self.assertIn('Sorry, you do not have enough chips!', output)
        self.assertEqual(chips.bet, 30)


if __name__ == '__main__':
    unittest.main()
