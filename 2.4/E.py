zyika_count = 0
current_suburb = []


def main(current_sight):
    """
    Updates the zyika count based on the current sight.

    Args:
        current_sight (str): The current sight in the suburb.

    Returns:
        None
    """
    global zyika_count, total_suburbs, current_suburb

    if current_sight == "ВСЁ":
        total_suburbs -= 1
        if "зайка" in current_suburb:
            zyika_count += 1
        current_suburb = []
    else:
        current_suburb.append(current_sight)
    return None


if __name__ == "__main__":
    total_suburbs = int(input())
    while total_suburbs != 0:
        main(current_sight=input())
    print(zyika_count)
