from classes import room

UL_START = "\033[04m"
UL_END = "\033[0m"


def main():
    garden = room.Room("Garden", "A beautiful garden with a fountain.")
    kitchen = room.Room("Kitchen", "A small kitchen with a table and chairs.")

    garden.e_to = kitchen
    kitchen.w_to = garden

    print(garden)
    print(kitchen)


if __name__ == "__main__":
    main()

