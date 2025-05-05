def calc(a, b, op):
    """
    Returns a string like this: a op b = c
    where c is the computed value, according to the operator
    """
    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    if op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    if op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    if op == '/':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)


def main():
    """
    Asks the user to input two numbers.
    Converts them into integers.
    Asks the user which arithmetic operation to perform.
    Prints the result returned by calc() (e.g., "2 + 3 = 5" or an error message for invalid operators).
    """
    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    if op not in '+-/*':
        print("Please restart and only type one of these characters: '+, -, *, /'!")

    print(calc(a, b, op))


if __name__ == '__main__':
    main()
