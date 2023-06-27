def main(name, price, weight, money):
    """
    Calculates the change and prints the receipt for a purchase.

    Args:
        name (str): The name of the item.
        price (int): The price per kilogram of the item.
        weight (int): The weight of the item in kilograms.
        money (int): The amount of money provided by the customer.

    Returns:
        None
    """
    total = price * weight
    change = money - total

    print("Чек")
    print(f"{name} - {weight}кг - {price}руб/кг")
    print(f"Итого: {total}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {change}руб")


if __name__ == "__main__":
    n = input()
    p = int(input())
    w = int(input())
    m = int(input())
    main(name=n, price=p, weight=w, money=m)
