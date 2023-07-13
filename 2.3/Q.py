def main(num):
    """
    """
    for idx, el in enumerate(num):
        if int(el) % 2 == 0:
            num = num[:idx] + "_" + num[idx + 1:]
    print(num.replace("_", ""))


if __name__ == "__main__":
    long_num = input()
    main(num=long_num)
