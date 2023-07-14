from itertools import combinations

numbers = list()


def nod(a, b):
    """
    """
    while b != 0:
        a, b = b, a % b
    return a


def main(numbers):
    """
    """
    if len(set(numbers)) == 1:
        return print(numbers[0])
    nods = []
    pairs = combinations(numbers, 2)

    for pair in pairs:
        nods.append(nod(*pair))

    return main(nods)


if __name__ == "__main__":
    for i in range(int(input())):
        numbers.append(int(input()))
    main(numbers=numbers)
