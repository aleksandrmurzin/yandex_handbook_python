def main(number):
    """
    """
    if number == 1:
        return print("NO")

    for i in range(1, number + 1):
        if number % i == 0 and i not in [1, number]:
            return print("NO")
    return print("YES")


if __name__ == "__main__":
    number = int(input())
    main(number=number)
