def main(num):
    """
    Prints combinations of letters based on the given number.

    Args:
        num (int): The total number of letters.

    Returns:
        None
    """
    print("А Б В")
    comb = [1, 1] + [num - 2]
    print(" ".join(map(str, comb)))
    for i in range(len(comb) - 1, 0, -1):
        while comb[i] != 1:
            comb[i - 1] += 1
            comb[i] -= 1
            print(" ".join(map(str, comb)))

if __name__ == "__main__":
    num = int(input())
    main(num=num)
