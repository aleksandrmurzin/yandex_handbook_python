def main(n):
    """
    Prints the message "Купи слона!" n times without a trailing empty line.

    Args:
        n (int): The number of times to print the message.

    Returns:
        None
    """
    print(f"Купи слона!\n" * n, end="")


if __name__ == '__main__':
    n = int(input())
    main(n=n)