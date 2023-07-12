x, y = 0, 0

steps = {
    "СЕВЕР": 0,
    "ВОСТОК": 0,
    "ЮГ": 0,
    "ЗАПАД": 0
}


def main():
    """
    Calculate the final position coordinates based on the accumulated steps in different directions.

    Updates the global variables 'x' and 'y' with the calculated coordinates based on the steps accumulated in the 'steps' dictionary.

    Returns:
        None
    """
    global x, y
    x = steps["ВОСТОК"] - steps["ЗАПАД"]
    y = steps["СЕВЕР"] - steps["ЮГ"]


if __name__ == "__main__":
    while (direction := input()) != "СТОП":
        step = int(input())
        steps[direction] += step
    main()
    print(y, x, sep="\n")
