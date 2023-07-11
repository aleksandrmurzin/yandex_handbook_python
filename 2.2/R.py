def main(a, b, c):
    """
    Checks if the given triangle with sides a, b, and c is a right triangle.

    Args:
        a (int): Length of side a.
        b (int): Length of side b.
        c (int): Length of side c.

    Prints:
        "100%" if the triangle is a right triangle.
        "крайне мала" if the triangle is acute.
        "велика" if the triangle is obtuse.
    """
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("100%")
    elif sides[0] ** 2 + sides[1] ** 2 > sides[2] ** 2:
        print("крайне мала")
    else:
        print("велика")


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    main(a=a, b=b, c=c)
