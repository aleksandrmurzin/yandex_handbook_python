def main(start, end, step=1):
    """
    Print numbers from 'start' to 'end', inclusive, with a specified step.

    Args:
        start (int): The starting number.
        end (int): The ending number.
        step (int, optional): The step size between numbers. Defaults to 1.

    Returns:
        None
    """
    if end < start:
        step = -1

    [print(i, end=' ') for i in range(start, end + step, step)]


if __name__ == "__main__":
    start = int(input())
    end = int(input())
    main(start=start, end=end)
