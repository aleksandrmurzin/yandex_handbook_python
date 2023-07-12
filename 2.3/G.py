if __name__ == "__main__":
    a = int(input())
    b = int(input())

    a_init = a
    b_init = b

    while b != 0:
        a, b = b, a % b
    print(f"{(a_init * b_init / a):.0f}")
