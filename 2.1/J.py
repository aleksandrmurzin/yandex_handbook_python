def main(name, code):
    """
    Prints the information about a person's group, index, name, code, and bed.

    Args:
        name (str): The person's name.
        code (str): The group, bed, and index code as a string, separated by commas.

    Returns:
        None
    """
    group, bed, index = code
    print(f"Группа №{group}.")
    print(f"{index}. {name}.")
    print(f"Шкафчик: {code}.")
    print(f"Кроватка: {bed}.")
    return None


if __name__ == '__main__':
    n = input()
    c = input()
    main(name=n, code=c)
