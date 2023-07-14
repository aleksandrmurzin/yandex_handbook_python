init_count = 3


def main(num_bikers):
    """
    Simulates a bike race countdown and start for the given number of bikers.

    Args:
        num_bikers (int): The number of bikers in the race.

    Returns:
        None
    """
    global init_count

    for biker in range(1, num_bikers + 1):
        for s in range(init_count, 0, -1):
            print(f"До старта {s} секунд(ы)")
        print(f"Старт {biker}!!!")
        init_count += 1
    return None


if __name__ == "__main__":
    num_bikers = int(input())
    main(num_bikers=num_bikers)
