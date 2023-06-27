def main(price, weight, customer_money):
    """
    Calculates the customer's remaining money after purchasing an item.

    Args:
        price (int): The price of the item.
        weight (int): The weight of the item.
        customer_money (int): The amount of money the customer has.

    Returns:
        None
    """
    total_price = price * weight
    customer_money_left = customer_money - total_price
    print(customer_money_left)


if __name__ == '__main__':
    p = int(input())
    w = int(input())
    c = int(input())
    main(price=p, weight=w, customer_money=c)
