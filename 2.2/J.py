def main(password):
    """
    Splits the given password into two halves, calculates the sum of each half,
    sorts the sums in descending order, and prints the resulting ciphered password.

    Args:
        password (str): The input password to be processed.

    Returns:
        None
    """
    password_array = list(password)
    first_password_half = password_array[:2]
    second_password_half = password_array[1:]

    first_half_sum = sum([int(i) for i in first_password_half])
    second_half_sum = sum([int(i) for i in second_password_half])

    syphered_pass = "".join(
        [str(i) for i in sorted([first_half_sum, second_half_sum], reverse=True)])
    print(syphered_pass)


if __name__ == "__main__":
    given_password = input()
    main(password=given_password)
