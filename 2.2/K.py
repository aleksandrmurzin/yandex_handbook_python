def main(digit):
    """
    Checks if a given digit meets a specific condition.

    The function takes a digit as input and checks if the sum of the largest and smallest digit
    is equal to twice the remaining digit. If the condition is met, it prints "YES", otherwise it prints "NO".

    Args:
        digit (str): The input digit.

    Returns:
        None
    """
    digit_array = [int(i) for i in list(digit)]
    max_num = max(digit_array)
    min_num = min(digit_array)
    digit_array.remove(max_num)
    digit_array.remove(min_num)
    mean_num = digit_array[0]

    if max_num + min_num == mean_num * 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    given_digit = input()
    main(digit=given_digit)
