from itertools import permutations


def main(number):
    """
    Prints the minimum and maximum combinations of two digits from the given number.

    Parameters:
    number (str): The input number as a string.

    Returns:
    None
    """
    array = list(number)
    integer_combinations = [int(''.join(i)) for i in permutations(
        array, 2) if int(''.join(i)) >= 10]
    min_combination = min(integer_combinations)
    max_combination = max(integer_combinations)
    print(min_combination, max_combination)


if __name__ == "__main__":
    magic_number = input()
    main(number=magic_number)
