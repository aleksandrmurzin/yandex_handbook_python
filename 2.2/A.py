def main(name, mood):
    """
    Entry point of the program.

    Args:
        name (str): The name of the user.
        mood (str): The mood of the user.

    Returns:
        None
    """
    print("Как Вас зовут?")
    print(f"Здравствуйте, {name}!")
    print("Как дела?")
    match mood:
        case "хорошо":
            print("Я за вас рада!")
        case "плохо":
            print("Всё наладится!")


if __name__ == "__main__":
    name = input()
    mood = input()
    main(name=name, mood=mood)
