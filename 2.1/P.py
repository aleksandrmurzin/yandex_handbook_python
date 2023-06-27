def main(warehouse, store, speed):
    """
    Entry point of the program.

    Args:
        warehouse (int): The position of the warehouse.
        store (int): The position of the store.
        speed (int): The average speed of travel.
    """
    distance = store - warehouse
    time = distance / speed
    print(f"{time:.2f}")


if __name__ == "__main__":
    warehouse_position = int(input())
    store_position = int(input())
    avg_speed = int(input())
    main(warehouse=warehouse_position, store=store_position, speed=avg_speed)
