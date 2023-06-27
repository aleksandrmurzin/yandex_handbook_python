def main(hour, minute, order_minute):
    """
    Entry point of the program.
    
    Args:
        curr_hour (int): The current hour.
        curr_minute (int): The current minute.
        order_minute (int): The minutes for the order to come.
    """
    total_minutes = hour * 60 + minute
    order_arrival_minutes = total_minutes + order_minute

    order_arrival_hour = order_arrival_minutes // 60
    order_arrival_minute = order_arrival_minutes % 60
    if order_arrival_hour > 24:
        order_arrival_hour = order_arrival_hour % 24
    print(f"{str(order_arrival_hour).zfill(2)}:{str(order_arrival_minute).zfill(2)}")


if __name__ == "__main__":
    curr_hour = int(input())
    curr_minute = int(input())
    order_minute = int(input())
    main(hour=curr_hour, minute=curr_minute, order_minute=order_minute)
