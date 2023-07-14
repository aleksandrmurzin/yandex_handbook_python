def main(table_size):
    """
    Prints a multiplication table of the given size.

    Args:
        table_size (int): The size of the multiplication table.

    Returns:
        None
    """
    for i in range(1, table_size + 1):
        print(" ".join(map(str, list(range(i, i * table_size + 1, i)))))


if __name__ == "__main__":
    table_size = int(input())
    main(table_size=table_size)
