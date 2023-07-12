factorial = 1


def main(n):
    """
    Calculate the factorial of a number.

    Given a number 'n', the function calculates its factorial by multiplying 'factorial' with 'n' and then decrementing 'n' by 1.

    Args:
        n (int): The number for which factorial is calculated.

    Returns:
        int: The updated value of 'n' after decrementing by 1.
    """
    global factorial

    factorial *= n
    n -= 1
    return n


if __name__ == "__main__":
    n = int(input())
    while n > 1:
        n = main(n=n)
    print(factorial)
