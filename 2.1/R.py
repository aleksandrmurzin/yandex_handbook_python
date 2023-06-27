def main(cost, banknote):
    """
    Calculate and print the change to be given back.

    Args:
        cost (int): The total cost of the purchase.
        banknote (int): The amount paid by the customer.

    Returns:
        None
    """
    change = banknote - cost
    print(f"{change}")


if __name__ == "__main__":
    cost = int(input(), 2)
    banknote = int(input())
    main(cost=cost, banknote=banknote)
