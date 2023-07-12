def main(start, end):
    """
    Print numbers from 'start' to 'end', inclusive.

    Args:
        start (int): The starting number.
        end (int): The ending number.

    Returns:
        None
    """
    [print(i, end=' ') for i in range(start, end + 1, 1)]


if __name__ == "__main__":
    start = int(input())
    end = int(input())
    main(start=start, end=end)
