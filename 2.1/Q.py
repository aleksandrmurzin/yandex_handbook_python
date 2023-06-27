def main(curr_amount, last_order):
    """
    Update the current amount with the last order and print the result.

    Args:
        curr_amount (int): The current amount.
        last_order (int): The last order to add to the current amount.
    """
    curr_amount += last_order
    print(f"{curr_amount}")


if __name__ == "__main__":
    curr = int(input())
    last = int(input(), 2)
    main(curr_amount=curr, last_order=last)
