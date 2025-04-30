from IPython.display import clear_output
import random


def display_board(board):
    """
    Prints out a board, where each index 1-9 corresponds with a number on a number pad.
    So you get a 3 by 3 board representation.
    """
    clear_output()
    print(f"\n\t {board[7]} | {board[8]} | {board[9]}")
    print("\t", "---------")
    print(f"\n\t {board[4]} | {board[5]} | {board[6]}")
    print("\t", "---------")
    print(f"\n\t {board[1]} | {board[2]} | {board[3]}\n")


def player_input():
    """
    Takes in a player input and assigns their marker as 'X' or 'O'.
    The while loop continually asks until you get a correct answer.
    """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, please choose X or O: ')

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def place_marker(board, marker, position):
    """
    Takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9).
    Assigns it to the board.
    """
    board[position] = marker
    return board


def win_check(board, mark):
    """
    Takes in a board and a mark (X or O).
    Then checks to see if that mark has won.
    """
    for win in board:
        if board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark:
            return True
        elif board[7] == board[8] == board[9] == mark or board[1] == board[4] == board[7] == mark:
            return True
        elif board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark:
            return True
        elif board[3] == board[5] == board[7] == mark or board[1] == board[5] == board[9] == mark:
            return True
        else:
            return False


def choose_first():
    """
    Uses the random module to randomly decide which player goes first.
    Returns a string of which player will go first.
    """
    if random.randint(0, 1) % 2 == 0:
        return 'Player1'
    else:
        return 'Player2'


def space_check(board, position):
    """
     Returns a boolean indicating whether a space on the board is freely available.
    """
    return board[position] == ' '


def full_board_check(board):
    """
    Checks if the board is full and returns a boolean value.
    True if full, False otherwise.
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    """
    Asks for a player's next position (as a number 1-9).
    Then uses the function space_check to check if it's a free position.
    If it is, then returns the position for later use.
    """
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Choose your next position (1-9): '))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    return position


def replay():
    """
    Asks the player if they want to play again.
    Returns a boolean True if they do want to play again, and False if they don't.
    """
    choice = 'wrong'

    while choice not in ['Yes', 'No']:
        choice = input('Do you want to keep playing? (Yes or No) ')

        if choice not in ['Yes', 'No']:
            print('Sorry, I do not understand, please choose Yes or No')

    if choice == "Yes":
        return True
    else:
        return False


def run_game():
    """
    Uses while loops and the functions made to run the game!
    """
    print('Welcome to Tic Tac Toe!')
    while True:
        the_board = [' '] * 10
        player1_marker, player2_marker = player_input()

        turn = choose_first()
        print(turn + ' will go first.')
        play_game = input('Ready to play? yes or no? ')

        if play_game == 'yes':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Player 1 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie game!')
                        game_on = False
                    else:
                        turn = 'Player 2'
            else:
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie game!')
                        game_on = False
                    else:
                        turn = 'Player 1'

        if not replay():
            print('Thank you for playing!')
            break


if __name__ == "__main__":
    run_game()
