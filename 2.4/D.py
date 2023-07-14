total_sum = 0


def main(current_number):
    """
    Updates the total sum by adding the sum of digits in the current number.

    Args:
        current_number (str): The current number.

    Returns:
        None
    """
    global counter, total_sum

    total_sum += sum([int(i) for i in current_number])
    counter -= 1


if __name__ == "__main__":
    counter = int(input())
    while counter != 0:
        main(current_number := input())
    print(total_sum)
