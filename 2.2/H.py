def main(seq):
    """
    Check if the word "зайка" is present in the given sequence.

    Parameters:
    seq (str): A string containing a sequence of words.

    Prints:
    "YES" if the word "зайка" is present in the sequence, otherwise "NO".
    """
    if "зайка" in seq.split(" "):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    given_seq = input()
    main(seq=given_seq)
