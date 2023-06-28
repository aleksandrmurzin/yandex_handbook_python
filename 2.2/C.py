def main(petya_avg_speed, vasya_avg_speed, tolya_avg_speed):
    """
    Prints the name of the participant with the highest average speed.

    Args:
        petya_avg_speed (int): The average speed of participant Петя.
        vasya_avg_speed (int): The average speed of participant Вася.
        tolya_avg_speed (int): The average speed of participant Толя.

    Returns:
        None
    """
    final_results = {
        'Петя': petya_avg_speed,
        'Вася': vasya_avg_speed,
        'Толя': tolya_avg_speed
    }

    winner_name = max(final_results, key=final_results.get)
    print(winner_name)


if __name__ == "__main__":
    petya_avg_speed = int(input())
    vasya_avg_speed = int(input())
    tolya_avg_speed = int(input())
    main(petya_avg_speed=petya_avg_speed,
         vasya_avg_speed=vasya_avg_speed, tolya_avg_speed=tolya_avg_speed)
