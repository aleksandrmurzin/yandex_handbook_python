def main(number_1, number_2):
    """
    Takes two numbers as input, combines their digits into an array,
    finds the maximum and minimum numbers in the array, removes them,
    calculates the sum of the remaining numbers, and prints the result
    in the format 'max_number + sum_of_remaining_numbers + min_number'.

    Args:
        number_1 (str): The first number.
        number_2 (str): The second number.

    Returns:
        None
    """
    numbers_array = list(map(int, list(number_1) + list(number_2)))
    max_number = max(numbers_array)
    min_number = min(numbers_array)

    numbers_array.remove(max_number)
    numbers_array.remove(min_number)
    middle_number = str(sum(numbers_array))[-1]
    print(f"{max_number}{middle_number}{min_number}")


if __name__ == "__main__":
    magic_number_1 = input()
    magic_number_2 = input()
    main(number_1=magic_number_1, number_2=magic_number_2)
