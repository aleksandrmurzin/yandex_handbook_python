def main(first, second):
    """
    Entry point of the program.
    
    Args:
        first (str): The first input.
        second (str): The second input.
    """
    first = first.zfill(3)
    second = second.zfill(3)

    ones = str(int(first[2]) + int(second[2]))[-1]
    tens = str(int(first[1]) + int(second[1]))[-1]
    hunderds = str(int(first[0]) + int(second[0]))[-1]

    print(f"{hunderds}{tens}{ones}")


if __name__ == "__main__":
    first = input()
    second = input()
    main(first=first, second=second)
