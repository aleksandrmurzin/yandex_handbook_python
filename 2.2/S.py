def main(x, y):
    """Main function to determine safety zone based on coordinates.

    Args:
        x (float): X-coordinate.
        y (float): Y-coordinate.
    """
    def solve_eq():
        """Solves the equation based on the input coordinate.

        Returns:
            float: Value of y for the equation.
        """
        y_eq = 0.25 * x ** 2 + 0.5 * x - 8.75
        return y_eq

    if x ** 2 + y ** 2 > 100:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    elif x >= 0 and y >= 0:
        if x ** 2 + y ** 2 > 25:
            print("Зона безопасна. Продолжайте работу.")
        else:
            print("Опасность! Покиньте зону как можно скорее!")
    elif x < 0 and y >= 0:
        if y > 5 or x < -7:
            print("Зона безопасна. Продолжайте работу.")
        elif x >= - 4 and y <= 5:
            print("Опасность! Покиньте зону как можно скорее!")
        elif (-3 * (y - 5)) - (-5 * (x - -4)) < 0:
            print("Зона безопасна. Продолжайте работу.")
        else:
            print("Опасность! Покиньте зону как можно скорее!")
    elif y < 0:
        if x < 5 and x > - 7:
            if solve_eq() > y:
                print("Зона безопасна. Продолжайте работу.")
            else:
                print("Опасность! Покиньте зону как можно скорее!")
        else:
            print("Зона безопасна. Продолжайте работу.")


if __name__ == "__main__":
    x = float(input())
    y = float(input())
    main(x=x, y=y)
