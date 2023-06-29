def main(petya_avg_speed, vasya_avg_speed, tolya_avg_speed):
    """
    Print the results of a race between Petya, Vasya, and Tolya.

    Args:
        petya_avg_speed (int): Average speed of Petya.
        vasya_avg_speed (int): Average speed of Vasya.
        tolya_avg_speed (int): Average speed of Tolya.
    """
    final_results = {
        'Петя': petya_avg_speed,
        'Вася': vasya_avg_speed,
        'Толя': tolya_avg_speed
    }

    names = sorted(final_results, key=final_results.get, reverse=True)
    first_place = names[0]
    second_place = names[1]
    third_place = names[2]

    print(f"{'': ^8}{first_place: ^8}{'': ^8}")
    print(f"{second_place: ^8}{'': ^8}{'': ^8}")
    print(f"{'': ^8}{'': ^8}{third_place: ^8}")
    print(f"{'II': ^8}{'I': ^8}{'III': ^8}")


if __name__ == "__main__":
    petya_avg_speed = int(input())
    vasya_avg_speed = int(input())
    tolya_avg_speed = int(input())
    main(petya_avg_speed=petya_avg_speed,
         vasya_avg_speed=vasya_avg_speed, tolya_avg_speed=tolya_avg_speed)
