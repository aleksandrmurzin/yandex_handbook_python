def main(seq1, seq2, seq3):
    """
    Check if the word "зайка" is present in the given sequence.

    Parameters:
    seq (str): A string containing a sequence of words.

    Prints:
    "YES" if the word "зайка" is present in the sequence, otherwise "NO".
    """
    seqs = []
    for seq in [seq1, seq2, seq3]:
        if "зайка" in seq.split(" "):
            seqs.append(seq)
    min_seq = sorted(seqs)[0]
    min_length = len(min_seq)
    print(f"{min_seq} {min_length}")


if __name__ == "__main__":
    given_seq1 = input()
    given_seq2 = input()
    given_seq3 = input()
    main(seq1=given_seq1, seq2=given_seq2, seq3=given_seq3)
