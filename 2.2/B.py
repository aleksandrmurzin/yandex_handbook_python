def main(petya_avg_speed, vasya_avg_speed):
    """
    Entry point of the program.

    Args:
        petya_avg_speed (int): Average speed of Petya.
        vasya_avg_speed (int): Average speed of Vasya.

    Returns:
        None
    """
    if petya_avg_speed > vasya_avg_speed:
        print('Петя')
    else:
        print('Вася')


if __name__ == "__main__":
    petya_avg_speed = int(input())
    vasya_avg_speed = int(input())
    main(petya_avg_speed=petya_avg_speed, vasya_avg_speed=vasya_avg_speed)
