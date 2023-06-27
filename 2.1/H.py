def main(n, phrase):
    """
    Prints the given phrase 'n' times without a trailing empty line.

    Args:
        n (int): The number of times to print the phrase.
        phrase (str): The phrase to be printed.

    Returns:
        None
    """
    print(f'Я больше никогда не буду писать "{phrase}"!\n' * n, end="")


if __name__ == '__main__':
    n = int(input())
    p = input()
    main(n=n, phrase=p)