def main(tree_elements):
    """
    Prints a tree structure based on the given number of elements.

    Args:
        tree_elements (int): The number of elements in the tree.

    Returns:
        None
    """
    row = 1
    currnetn_row = []

    for i in range(1, tree_elements + 1):
        if len(currnetn_row) < row:
            currnetn_row.append(i)
        else:
            print(" ".join(map(str, currnetn_row)))
            currnetn_row = [i]
            row += 1
    print(" ".join(map(str, currnetn_row)))

    return None


if __name__ == "__main__":
    tree_elements = int(input())
    main(tree_elements=tree_elements)
