children = []


def main(children):
    """
    Prints the name of the child with the maximum sum of numbers.

    Args:
        children (list): List of tuples containing child names and corresponding numbers.

    Returns:
        None
    """
    child_with_max_num = ""
    max_num = 0
    for child in children:
        if child[1] >= max_num:
            max_num = child[1]
            child_with_max_num = child[0]

    print(child_with_max_num)
    return None


if __name__ == "__main__":
    for i in range(int(input())):
        name = input()
        num = sum([int(y) for y in input()])
        children.append(tuple([name, num]))

    main(children=children)
