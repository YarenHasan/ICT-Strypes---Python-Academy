import random


def flip():
    """
    Simulates a coin flip.
    Generates a random float number between 0.0 and 1.0.
    """
    flip = random.random()
    if flip >= .5:
        return True
    else:
        return False


def main(num):
    """
    Performs multiple coin flips and tracks the results.
    Initializes counters for heads and tails.
    Initializes a string to record the flip sequence.
    """
    heads = 0
    tails = 0
    resultString = " "

    for i in range(int(num)):
        if flip():
            heads += 1
            resultString += " H "
        else:
            tails += 1
            resultString += " T "

    print("Number of Heads: %i" % heads)
    print("Number of Tails: %i" % tails)
    print(resultString)


userInput = input("Please enter a number of flips: ")
main(userInput)
