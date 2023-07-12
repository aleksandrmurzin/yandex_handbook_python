total = 0


def main(price):
    """
    Calculate the total price after applying discounts.

    If the price is equal to or greater than 500, a 10% discount is applied.

    Args:
        price (float): The price of an item.

    Returns:
        None
    """
    global total

    if price >= 500:
        price *= 0.9

    total += price


if __name__ == "__main__":
    while (price := float(input())) != 0:
        main(price=price)
    print(total)
