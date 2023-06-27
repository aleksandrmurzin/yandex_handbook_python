def main(red, blue):
    """
    Calculates the sum of the given red and blue values, incremented by 1.

    Args:
        red (int): The value of red.
        blue (int): The value of blue.
    """
    answer = red+blue+1
    print(f"{answer}")
    return None


if __name__ == "__main__":
    red = int(input())
    _ = int(input())
    blue = int(input())
    main(red=red, blue=blue)
