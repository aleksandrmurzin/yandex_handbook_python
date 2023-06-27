def main(item_name, price_per_kg, weight_kg, amount_paid):
    """
    Calculates the change and prints the receipt for a purchase.

    Args:
        item_name (str): The name of the item.
        price_per_kg (int): The price per kilogram of the item.
        weight_kg (int): The weight of the item in kilograms.
        amount_paid (int): The amount of money provided by the customer.

    Returns:
        None
    """
    total_cost = price_per_kg * weight_kg
    change = amount_paid - total_cost

    len_item = 35 - len("Товар:")
    len_price = 35 - len("Цена:") - len("кг") - len(" * ") - \
        len(str(price_per_kg)) - len("руб/кг")
    len_total = 35 - len("Итого:") - len("руб")
    len_paid = 35 - len("Внесено:") - len("руб")
    len_change = 35 - len("Сдача:") - len("руб")

    receipt_header = "Чек"
    print(f"{receipt_header:=^35}")
    print(f"Товар:{item_name: >{len_item}}")
    print(f"Цена:{weight_kg: >{len_price}}кг * {price_per_kg}руб/кг")
    print(f"Итого:{total_cost: >{len_total}}руб")
    print(f"Внесено:{amount_paid: >{len_paid}}руб")
    print(f"Сдача:{change: >{len_change}}руб")
    print("=" * 35)


if __name__ == "__main__":
    item = input()
    price = int(input())
    weight = int(input())
    money = int(input())
    main(item_name=item, price_per_kg=price,
         weight_kg=weight, amount_paid=money)
