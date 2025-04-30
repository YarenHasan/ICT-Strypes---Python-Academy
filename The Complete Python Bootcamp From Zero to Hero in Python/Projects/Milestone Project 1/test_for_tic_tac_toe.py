import unittest
from unittest.mock import patch
import builtins
from tic_tac_toe import (
    place_marker,
    win_check,
    choose_first,
    space_check,
    full_board_check,
    player_input,
    player_choice,
    replay
)


class TestTicTacToe(unittest.TestCase):

    def test_place_marker(self):
        """
        Tests whether the place_marker function correctly places a marker on the board at given position.
        """
        board = [' '] * 10
        expected = [' '] * 10
        expected[5] = 'X'
        result = place_marker(board, 'X', 5)
        self.assertEqual(result, expected)

    def test_win_check_rows(self):
        """
        Tests if the win_check function correctly detects a winning condition across a row.
        """
        board = [' '] * 10
        board[1:4] = ['X', 'X', 'X']
        self.assertTrue(win_check(board, 'X'))

    def test_win_check_columns(self):
        """
        Tests if the win_check function correctly detects a winning condition for a column.
        """
        board = [' '] * 10
        board[1] = board[4] = board[7] = 'O'
        self.assertTrue(win_check(board, 'O'))

    def test_win_check_diagonals(self):
        """
        Tests if the win_check function correctly detects a winning condition for a diagonal.
        """
        board = [' '] * 10
        board[1] = board[5] = board[9] = 'X'
        self.assertTrue(win_check(board, 'X'))

    def test_win_check_false(self):
        """
        Ensures that win_check() returns False when there is no winning combination.
        """
        board = [' '] * 10
        board[1] = board[2] = board[4] = 'X'
        self.assertFalse(win_check(board, 'X'))

    def test_space_check_true(self):
        """
        Tests if space_check() correctly returns True when a board position is empty.
        """
        board = [' '] * 10
        self.assertTrue(space_check(board, 3))

    def test_space_check_false(self):
        """
        Tests that space_check() returns False when a position is already occupied.
        """
        board = [' '] * 10
        board[3] = 'O'
        self.assertFalse(space_check(board, 3))

    def test_full_board_check_true(self):
        """
        Tests full_board_check() to verify it detects a filled board (no empty spaces left).
        """
        board = [' '] + ['X'] * 9
        self.assertTrue(full_board_check(board))

    def test_full_board_check_false(self):
        """
        Verifies that full_board_check() returns False when at least one space is empty.
        """
        board = [' '] + ['X'] * 8 + [' ']
        self.assertFalse(full_board_check(board))

    def test_choose_first_randomness(self):
        """
        Tests if choose_first() correctly returns:
        'Player1' when random.randint() is mocked to return 0.
        'Player2' when mocked to return 1.
        """
        with patch('random.randint', return_value=0):
            self.assertEqual(choose_first(), 'Player1')
        with patch('random.randint', return_value=1):
            self.assertEqual(choose_first(), 'Player2')

    @patch('builtins.input', side_effect=['X'])
    def test_player_input_choice_X(self, mock_input):
        """
        Tests player_input() function, ensuring:
        Choosing 'X' gives ('X', 'O').
        """
        self.assertEqual(player_input(), ('X', 'O'))

    @patch('builtins.input', side_effect=['O'])
    def test_player_input_choice_O(self, mock_input):
        """
        Tests player_input() function, ensuring:
        Choosing 'O' gives ('O', 'X').
        """
        self.assertEqual(player_input(), ('O', 'X'))

    @patch('builtins.input', side_effect=['5'])
    def test_player_choice_valid(self, mock_input):
        """
        Tests player_choice() to see if it correctly accepts a valid input.
        """
        board = [' '] * 10
        self.assertEqual(player_choice(board), 5)

    @patch('builtins.input', side_effect=['invalid', '10', '5'])
    def test_player_choice_with_invalids(self, mock_input):
        """
        Tests how player_choice() handles invalid inputs like a string 'invalid', an out-of-range '10', and then accepts the valid input.
        """
        board = [' '] * 10
        self.assertEqual(player_choice(board), 5)

    @patch('builtins.input', side_effect=['Yes'])
    def test_replay_yes(self, mock_input):
        """
        Tests replay() function for:
        'Yes' → returns True.
        """
        self.assertTrue(replay())

    @patch('builtins.input', side_effect=['No'])
    def test_replay_no(self, mock_input):
        """
        Tests replay() function for:
        'No' → returns False.
        """
        self.assertFalse(replay())

    @patch('builtins.input', side_effect=['maybe', 'Yes'])
    def test_replay_invalid_then_yes(self, mock_input):
        """
        Tests replay() function for:
        Invalid input ('maybe') followed by 'Yes' → ultimately returns True.
        """
        self.assertTrue(replay())


if __name__ == '__main__':
    unittest.main()
