def main(name1, name2, name3):
    """
    Prints the smallest name among the given names.

    Args:
        name1 (str): The first name.
        name2 (str): The second name.
        name3 (str): The third name.
    """
    smallest_name = min(name1, name2, name3)
    print(smallest_name)


if __name__ == "__main__":
    given_name_1 = input()
    given_name_2 = input()
    given_name_3 = input()
    main(name1=given_name_1, name2=given_name_2, name3=given_name_3)
