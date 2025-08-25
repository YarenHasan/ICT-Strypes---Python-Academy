def fibonacci(n: int) -> list[int]:
    """
    Връща поредицата на Фибоначи до числото n включително.
    """
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    user_input = int(input("Въведи число: "))
    print(fibonacci(user_input))
