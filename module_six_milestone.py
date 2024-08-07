__author__ = "Dave Mobley"
__copyright__ = "Copyright 2024"
__credits__ = ["Dave Mobley"]
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Dave Mobley"

# Copied from the module six rubric
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}


def move(current_room, direction):
    """
    Move the player to a new room based on the given direction.

    Parameters:
    current_room (str): The name of the current room.
    direction (str): The direction in which the player wants to move.

    Returns:
    str: The name of the new room if the direction is valid, otherwise the current room.
    """
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print('You can\'t go that way!')
        return current_room


def print_room(current_room):
    """
    Print the name of the current room.

    Parameters:
    current_room (str): The name of the current room.
    """
    print('You are in the', current_room)


def play_game():
    """
    Start and run the dragon text game.

    This function initializes the game by setting the starting room and then enters a loop where it prompts the
    player for a direction to move. The player can move between rooms or exit the game by typing 'Quit' or 'Exit'.

    The valid directions are 'North', 'South', 'East', and 'West'. If an invalid direction is entered,
    an error message is displayed.

    The game continues until the player chooses to exit.

    Returns:
    None
    """
    current_room = 'Great Hall'
    print_room(current_room)
    while True:
        direction = input('Which direction would you like to go? ').strip().capitalize()
        if direction == 'Quit' or direction == 'Exit':
            print("Exiting game. Goodbye!")
            break
        elif direction in ['North', 'South', 'East', 'West']:
            current_room = move(current_room, direction)
            print_room(current_room)
        else:
            print("Invalid direction. Please enter 'North', 'South', 'East', or 'West'.")


# Run the game
play_game()
