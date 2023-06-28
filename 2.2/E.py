APPLES = {
    "Петя": 6,
    "Вася": 9
}


def main(apples_for_petya, apples_for_vasya):
    """
    Update apple counts for Петя and Вася, and determine who has the most apples.

    Args:
        apples_for_petya (int): The number of apples for Петя.
        apples_for_vasya (int): The number of apples for Вася.
    """
    global APPLES
    APPLES["Петя"] += apples_for_petya
    APPLES["Вася"] += apples_for_vasya
    most_apples_boy = max(APPLES, key=APPLES.get)
    print(most_apples_boy)


if __name__ == "__main__":
    apples_for_petya = int(input())
    apples_for_vasya = int(input())
    main(apples_for_petya=apples_for_petya, apples_for_vasya=apples_for_vasya)
