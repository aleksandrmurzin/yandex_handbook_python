players_names = []


def main(names):
    """
    """
    first_to_play = min(names)
    print(first_to_play)
    return None


if __name__ == "__main__":
    total_players = int(input())
    for i in range(total_players):
        players_names.append(input())
    main(names=players_names)
