import init


def main():

    # Initialize rooms
    rooms = init.rooms()
    init.assign_room_connections(rooms)

    # Initialize items
    items = init.items()
    init.assign_room_items(rooms, items)

    # Initialize player
    player = init.init_player()
    print(player.get_connections())

    # DEBUG
    # for k, v in rooms.items():
    #     print(v)
    #     print(v.get_connections())
    #     print(v.get_items())
    #     print()


if __name__ == "__main__":
    main()
