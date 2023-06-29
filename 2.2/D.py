def main(petya_avg_speed, vasya_avg_speed, tolya_avg_speed):
    """
    Prints the names of the participants ranked by their average speeds in ascending order.

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
    winner_list = sorted(final_results, key=final_results.get, reverse=True)
    for i in range(0, len(winner_list)):
        print(f"{i+1}. {winner_list[i]}")


if __name__ == "__main__":
    petya_avg_speed = int(input())
    vasya_avg_speed = int(input())
    tolya_avg_speed = int(input())
    main(petya_avg_speed=petya_avg_speed,
         vasya_avg_speed=vasya_avg_speed, tolya_avg_speed=tolya_avg_speed)
