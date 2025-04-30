# MILESTONE PROJECT 1
# Tic Tac Toe Game (Console-Based)
This is a simple command-line implementation of the classic Tic Tac Toe game written in Python. The game allows two players to take turns placing their markers (X or O) on a 3x3 board, with the objective of getting three of their marks in a row (horizontally, vertically, or diagonally).

Features:

	Two-player game mode (local multiplayer).
	Console-based board display using a number pad layout.
	Random player starter.
	Input validation to prevent invalid or occupied positions.
	Option to replay the game after each round.



How to Play:

	Run the script in a Python environment that supports IPython.display.clear_output().
	Player 1 chooses a marker (X or O), and Player 2 gets the remaining marker.
	Players take turns choosing positions on the board (1–9, like a number pad).
	The game announces a winner or a tie once the board is full or a winning condition is met.
	After the game ends, players are prompted whether they want to play again.



Board Layout Reference:

	The board positions correspond to the number pad as follows:
	 7 | 8 | 9
	-----------
 	 4 | 5 | 6
	-----------
 	 1 | 2 | 3




 Code Overview:
 
The script includes the following core functions:

display_board(board): Renders the current game board.

player_input(): Gets player marker choice.

place_marker(board, marker, position): Places a marker on the board.

win_check(board, mark): Checks for a winning condition.

choose_first(): Randomly selects the first player.

space_check(board, position): Checks if a position is free.

full_board_check(board): Checks for a tie.

player_choice(board): Gets valid input for the next move.

replay(): Asks players if they want to play again.

run_game(): Main game loop.


Example:

Welcome to Tic Tac Toe!
Player 1, please choose X or O: X
Player2 will go first.
Ready to play? yes or no? yes

	   |   |  
	 ---------

	   |   |  
	 ---------

	   |   |  

Choose your next position (1-9): 1

	   |   |  
	 ---------

	   |   |  
	 ---------

	 O |   |  

Choose your next position (1-9): 5

	   |   |  
	 ---------

	   | X |  
	 ---------

	 O |   |  

Choose your next position (1-9): 2

	   |   |  
	 ---------

	   | X |  
	 ---------

	 O | O |  

Choose your next position (1-9): 3

	   |   |  
	 ---------

	   | X |  
	 ---------

	 O | O | X

Choose your next position (1-9): 7

	 O |   |  
	 ---------

	   | X |  
	 ---------

	 O | O | X

Choose your next position (1-9): 4

	 O |   |  
	 ---------

	 X | X |  
	 ---------

	 O | O | X

Choose your next position (1-9): 6

	 O |   |  
	 ---------

	 X | X | O
	 ---------

	 O | O | X

Choose your next position (1-9): 8

	 O | X |  
	 ---------

	 X | X | O
	 ---------

	 O | O | X

Choose your next position (1-9): 9

	 O | X | O
	 ---------

	 X | X | O
	 ---------

	 O | O | X

Tie game!
Do you want to keep playing? (Yes or No)  No
Thank you for playing!
