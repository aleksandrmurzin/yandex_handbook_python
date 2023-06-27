def main(num, total):
    """
    Distributes candy equally among children and calculates the remaining candy.
    
    Args:
        num (int): The number of children.
        total (int): The total number of candies.
    """
    candy2child = total_candy // num_childen
    left_candy = total_candy % num_childen
    print(f"{candy2child}\n{left_candy}", end="")


if __name__ == "__main__":
    num_childen = int(input())
    total_candy = int(input())
    main(num=num_childen, total=total_candy)


