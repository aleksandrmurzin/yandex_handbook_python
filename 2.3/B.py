def main(line):
    """
    Increment the counter if the word "зайка" is present in the input line.

    Args:
        line (str): The input line to check.

    Returns:
        None
    """
    global counter

    if "зайка" in line.split(" "):
        counter += 1
    return None


if __name__ == "__main__":
    counter = 0
    while (line := input()) != "Приехали!":
        main(line=line)
    print(counter)
