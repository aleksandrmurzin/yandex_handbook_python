def main(array):
    """
    Entry point of the program.

    Reads an array from input and checks if it is a palindrome.
    Prints "YES" if the array is a palindrome, and "NO" otherwise.

    Args:
        array (str): The input array to check.
    """
    if array == array[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    given_array = input()
    main(array=given_array)
