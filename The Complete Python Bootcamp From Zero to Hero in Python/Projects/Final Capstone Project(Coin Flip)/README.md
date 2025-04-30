# FINAL CAPSTONE PROJECT 1
 # 🪙 Coin Flip Simulator (Python CLI)
This is a simple Python script that simulates flipping a coin multiple times. It allows the user to input how many times they’d like to flip a coin, then displays the number of heads, tails, and the sequence of results.

🎯 Features

  * Randomized outcomes using Python's random module
  * User-defined number of flips
  * Count of Heads and Tails
  * Output of full flip sequence (e.g., H T H H T ...)

🧠 How It Works

  * You’ll be prompted to enter how many times you want to flip the coin.
  * The program flips the coin that many times using a random number generator.
  * It counts and prints the number of Heads and Tails.
  * It displays a string representation of the full flip sequence.

🧱 Code Overview

  * flip():	Returns True for Heads and False for Tails using random()
  * main(num):	Executes num flips, counts results, and prints them
  * flip_coin():	Handles user input and initiates the flip process

💻 Example:

    Please enter a number of flips: 9
    Number of Heads: 5
    Number of Tails: 4
      T  H  T  T  H  H  H  T  H 
