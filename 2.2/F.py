def main(year):
    """
    Check if a year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        None

        """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    given_year = int(input())
    main(year=given_year)
