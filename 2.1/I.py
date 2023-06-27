def main(n, m):
    """
    Calculates the total amount of kolbasa needed for a given number of children.

    Args:
        n (int): The number of children.
        m (int): The average amount of kolbasa per child.

    Returns:
        None
    """
    kolbasa_per_child = n / 2
    total_kolbasa = kolbasa_per_child * m
    print(f"{total_kolbasa:.0f}")


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    main(n=n, m=m)
