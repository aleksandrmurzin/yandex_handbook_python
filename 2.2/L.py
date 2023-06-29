from itertools import combinations


def main(a, b, c):
    """
    Determines whether a triangle with given side lengths is possible.

    Args:
        a (int): Length of side a.
        b (int): Length of side b.
        c (int): Length of side c.

    Returns:
        None: Prints "YES" if a triangle is possible, "NO" otherwise.
    """
    sides = [a, b, c]
    sides_sum = sum(sides)
    sides_combinations = combinations(sides, 2)

    if all([sides_sum - i[0] - i[1] < i[0] + i[1] for i in sides_combinations]):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    main(a=a, b=b, c=c)
