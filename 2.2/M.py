def main(elf_number, gnome_number, human_number):
    """
    Prints the first element of the given numbers if they are equal, 
    otherwise prints the second element of the elf number.

    Args:
        elf_number (str): The elf number.
        gnome_number (str): The gnome number.
        human_number (str): The human number.
    """
    if elf_number[0] == gnome_number[0] == human_number[0]:
        print(elf_number[0])
    else:
        print(elf_number[1])


if __name__ == "__main__":
    elf_number = input()
    gnome_number = input()
    human_number = input()
    main(elf_number=elf_number, gnome_number=gnome_number,
         human_number=human_number)
