counter = 0


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
    total_lines = int(input())
    for i in range(total_lines):
        main(line=input())
    print(counter)
