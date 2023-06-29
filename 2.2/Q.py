def main(a, b, c):
    """    
    Calculates the solutions of a quadratic equation ax^2 + bx + c = 0.
    Prints the solutions in the format: "x1 x2" (if two distinct solutions exist)
    or "x1" (if only one solution exists).
    Prints "Infinite solutions" if the equation has infinitely many solutions.

    :param a: Coefficient of x^2.
    :param b: Coefficient of x.
    :param c: Constant term.
    """
    double_a = 2 * a
    disc = b ** 2 - double_a * 2 * c

    if all([a == 0, b == 0]):
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    elif disc == 0:
        x1 = -b / 2 / a
        print(f"{x1:.2f}")
    elif disc > 0:
        sqrt_disc = (disc) ** 0.5
        x1 = (-b - sqrt_disc) / double_a
        x2 = (-b + sqrt_disc) / double_a
        if x1 < x2:
            print(f"{x1:.2f} {x2:.2f}")
        else:
            print(f"{x2:.2f} {x1:.2f}")
    else:
        print("No solution")


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    main(a=a, b=b, c=c)
