def main(longnum):
    """
    """
    max_num = int(longnum[0])

    for i in longnum[1:]:
        if (curr_num := int(i)) > max_num:
            max_num = curr_num
    print(max_num)
    return None


if __name__ == "__main__":
    longnum = input()
    main(longnum=longnum)
