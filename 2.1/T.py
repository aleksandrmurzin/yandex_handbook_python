def main(a, b, c, d):
    """
    Prints pairs of numbers (x, y) where x * c + y * d is equal to a * b.

    Args:
        a (int): The value of 'a'.
        b (int): The value of 'b'.
        c (int): The value of 'c'.
        d (int): The value of 'd'.
    """
    for x in range(1, a):
        y = a - x
        if (x * c + y * d) == a * b:
            print(x, y)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    main(a, b, c, d)
