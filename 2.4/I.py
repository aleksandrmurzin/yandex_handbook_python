top_numbers = []


if __name__ == "__main__":
    for i in range(int(input())):
        num = max([int(y) for y in input()])
        top_numbers.append(num)
    total_number = "".join(map(str, top_numbers))
    print(total_number)
