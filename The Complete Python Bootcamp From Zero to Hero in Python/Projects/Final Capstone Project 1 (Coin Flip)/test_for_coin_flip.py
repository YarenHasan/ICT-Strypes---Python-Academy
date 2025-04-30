import unittest
from unittest.mock import patch
import builtins
import io
import sys
from coin_flip import flip_coin


class TestFlipCoin(unittest.TestCase):

    @patch('builtins.input', return_value='4')  # Simulate user entering '4'
    @patch('random.random', side_effect=[0.6, 0.4, 0.9, 0.1])  # Simulate: H, T, H, T
    def test_flip_coin_output(self, mock_random, mock_input):
        """
        Tests if the fip_coin() function:
        Handles user input correctly,
        Accurately simulates coin flips with random outcomes,
        Counts and prints the number of heads and tails as expected,
        Outputs the flip sequence as a string.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect stdout to capture prints

        flip_coin()  # Call the main function

        sys.stdout = sys.__stdout__  # Restore stdout

        output = captured_output.getvalue()

        # Check that output contains expected counts
        self.assertIn("Number of Heads: 2", output)
        self.assertIn("Number of Tails: 2", output)
        self.assertIn("H", output)
        self.assertIn("T", output)


if __name__ == '__main__':
    unittest.main()
