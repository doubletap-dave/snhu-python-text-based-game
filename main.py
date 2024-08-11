__author__ = "Dave Mobley"
__copyright__ = "Copyright 2024"
__credits__ = ["Dave Mobley"]
__license__ = "MIT"
__version__ = "0.2.3"
__maintainer__ = "Dave Mobley"


from dataclasses import dataclass, field
from typing import List, Optional

import keyboard
import logging
import random
import time

# Configure logging
logging.basicConfig(
    filename='game.log',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s'
)


# Classes
class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UL = "\033[4m"
    BU = "\033[1m\033[4m"
    END = "\033[0m"


c = Color()


@dataclass
class Item:
    name: str
    desc: str
    dex: int
    int: int
    wis: int
    exp: int

    def __str__(self):
        return f"{self.name}: '{self.desc}'"

    def __repr__(self):
        return f"{self.name}: '{self.desc}'"

    def get_stats(self):
        return self.dex, self.int, self.wis


@dataclass
class Player:
    name: str
    dex: int
    int: int
    wis: int
    exp: int
    level: int
    current_room: "Room"
    items: List[Item] = field(default_factory=list)
    exp_to_lvl_up: int = 10

    def move(self, direction):
        logging.debug(f"Player {self.name} attempting to move {direction}")
        self.current_room.move_player(direction)

    def __str__(self):

        return (
            f"\n{c.BU + self.name + c.END}, "
            f"{c.BOLD + 'Lvl' + c.END}: {c.CYAN + str(self.level) + c.END}"
            f" {c.BOLD + 'Exp' + c.END}: {c.GREEN + str(self.exp) + c.END}\n"
            f" {c.BOLD + 'Backpack' + c.END}: {self.items}\n"
            f" {c.BOLD + 'Dex' + c.END}: {c.YELLOW + str(self.dex) + c.END}\n"
            f" {c.BOLD + 'Int' + c.END}: {c.BLUE + str(self.int) + c.END}\n"
            f" {c.BOLD + 'Wis' + c.END}: {c.PURPLE + str(self.wis) + c.END}\n"
        )

    def __repr__(self):
        return self.__str__()

    def add_item(self, item):
        self.items.append(item)
        self.current_room.remove_item(item)
        self.add_experience(item.exp)

    def add_experience(self, exp):
        self.exp += exp
        print(f"\nYou ({c.BU + self.name + c.END}) gained {c.GREEN + str(exp) + c.END} experience points.")
        if self.exp >= self.exp_to_lvl_up:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_lvl_up
        print(f"You ({c.BU + self.name + c.END}) leveled up to level {c.CYAN + str(self.level) + c.END}!\n")


@dataclass
class Room:
    name: str
    desc: str
    north: Optional["Room"] = None
    south: Optional["Room"] = None
    east: Optional["Room"] = None
    west: Optional["Room"] = None
    items: List[Item] = field(default_factory=list)
    player: Optional[Player] = None

    def __str__(self):
        return f"{self.name}: \"{self.desc}\""

    def __repr__(self):
        return self.__str__()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            logging.debug(f"Removing item {item.name} from room {self.name}")
            self.items.remove(item)
        else:
            logging.error(f"Item {item.name} not found in room {self.name}")

    def get_items(self):
        return self.items

    def set_player(self, player):
        self.player = player

    def get_player(self):
        return self.player

    def get_connections(self):
        connections = []
        if self.north:
            connections.append("north")
        if self.south:
            connections.append("south")
        if self.east:
            connections.append("east")
        if self.west:
            connections.append("west")
        return connections

    def has_connection(self, direction):
        return getattr(self, direction) is not None

    def move_player(self, direction):
        if not self.player:
            logging.error("No player in the room to move.")
            return

        logging.debug(f"Attempting to move player {self.player.name} to the {direction}")
        if self.has_connection(direction):
            next_room = getattr(self, direction)
            next_room.set_player(self.player)
            self.player.current_room = next_room
            logging.debug(f"Player moved to {self.player.current_room.name}")
            self.set_player(None)
        else:
            logging.error("You can't go that way.")


# Initialization functions

def init_rooms():
    verdant_vestibule = Room("Verdant Vestibule", "a lush garden with a fountain and blooming flowers.")
    whispering_willows = Room("Whispering Willows", "a grove of ancient trees with leaves that whisper secrets.")
    mosaic_menagerie = Room("Mosaic Menagerie", "a room filled with colorful mosaics depicting fantastical creatures.")
    guardians_chamber = Room("Guardians Chamber", "a massive stone golem stands watch over a glowing artifact.")
    runic_rotunda = Room("Runic Rotunda", "a circular chamber with glowing runes etched into the walls.")
    forgotten_fountain = Room("Forgotten Fountain", "a tranquil pool surrounded by statues of ancient heroes.")
    sunken_sanctuary = Room("Sunken Sanctuary", "an underwater grotto with shimmering fish and coral.")
    overgrown_observatory = Room("Overgrown Observatory", "a tower with a telescope that peers into the stars.")
    echoing_arboretum = Room("Echoing Arboretum", "a vast hall filled with the sound of rustling leaves.")

    return {
        "verdant_vestibule": verdant_vestibule,
        "whispering_willows": whispering_willows,
        "mosaic_menagerie": mosaic_menagerie,
        "guardians_chamber": guardians_chamber,
        "runic_rotunda": runic_rotunda,
        "forgotten_fountain": forgotten_fountain,
        "sunken_sanctuary": sunken_sanctuary,
        "overgrown_observatory": overgrown_observatory,
        "echoing_arboretum": echoing_arboretum,
    }


def init_room_connections(rooms):
    rooms["whispering_willows"].east = rooms["mosaic_menagerie"]
    rooms["whispering_willows"].south = rooms["verdant_vestibule"]

    rooms["mosaic_menagerie"].east = rooms["guardians_chamber"]
    rooms["mosaic_menagerie"].south = rooms["runic_rotunda"]
    rooms["mosaic_menagerie"].west = rooms["whispering_willows"]

    rooms["guardians_chamber"].west = rooms["mosaic_menagerie"]

    rooms["verdant_vestibule"].north = rooms["whispering_willows"]
    rooms["verdant_vestibule"].east = rooms["runic_rotunda"]
    rooms["verdant_vestibule"].south = rooms["sunken_sanctuary"]

    rooms["runic_rotunda"].north = rooms["mosaic_menagerie"]
    rooms["runic_rotunda"].east = rooms["forgotten_fountain"]
    rooms["runic_rotunda"].west = rooms["verdant_vestibule"]
    rooms["runic_rotunda"].south = rooms["overgrown_observatory"]

    rooms["forgotten_fountain"].west = rooms["runic_rotunda"]
    rooms["forgotten_fountain"].south = rooms["echoing_arboretum"]

    rooms["sunken_sanctuary"].north = rooms["verdant_vestibule"]
    rooms["sunken_sanctuary"].east = rooms["overgrown_observatory"]

    rooms["overgrown_observatory"].west = rooms["sunken_sanctuary"]
    rooms["overgrown_observatory"].north = rooms["runic_rotunda"]
    rooms["overgrown_observatory"].east = rooms["echoing_arboretum"]

    rooms["echoing_arboretum"].west = rooms["overgrown_observatory"]
    rooms["echoing_arboretum"].north = rooms["forgotten_fountain"]


def init_items():
    items = {
        "enchanted_flute": Item(
            name="Enchanted Flute",
            desc="a slender flute that plays haunting melodies when the wind blows.",
            dex=2,
            int=0,
            wis=0,
            exp=10,
        ),
        "prismatic_lens": Item(
            name="Prismatic Lens",
            desc="a multifaceted lens that refracts light into a dazzling rainbow.",
            dex=0,
            int=2,
            wis=0,
            exp=10,
        ),
        "magical_stylus": Item(
            name="Magical Stylus",
            desc="a silver stylus that draws glowing runes in the air when used.",
            dex=0,
            int=0,
            wis=2,
            exp=10,
        ),
        "vial_of_glowing_water": Item(
            name="Vial of Glowing Water",
            desc="a glass vial filled with water that glows with an inner light.",
            dex=1,
            int=1,
            wis=1,
            exp=10,
        ),
        "weathered_stone_tablet": Item(
            name="Weathered Stone Tablet",
            desc="a stone tablet etched with ancient runes and symbols.",
            dex=1,
            int=1,
            wis=1,
            exp=10,
        ),
        "celestial_map": Item(
            name="Celestial Map",
            desc="a map of the stars that reveals hidden constellations.",
            dex=1,
            int=1,
            wis=1,
            exp=10,
        ),
        "resonance_crystal": Item(
            name="Resonance Crystal",
            desc="a crystal that hums with a mysterious energy when touched.",
            dex=1,
            int=1,
            wis=1,
            exp=10,
        ),
    }
    return items


def init_room_items(rooms, items):
    rooms["whispering_willows"].add_item(items["enchanted_flute"])
    rooms["mosaic_menagerie"].add_item(items["prismatic_lens"])
    rooms["runic_rotunda"].add_item(items["magical_stylus"])
    rooms["forgotten_fountain"].add_item(items["vial_of_glowing_water"])
    rooms["sunken_sanctuary"].add_item(items["weathered_stone_tablet"])
    rooms["overgrown_observatory"].add_item(items["celestial_map"])
    rooms["echoing_arboretum"].add_item(items["resonance_crystal"])


def init_player_stats():
    dex = random.randint(1, 10)
    int = random.randint(1, 10)
    wis = random.randint(1, 10)
    return dex, int, wis


def init_player(rooms):
    # Prompt the player to enter their name
    name = input("Hail Adventurer! Please enter your name: ").strip()

    # List of adventure-sounding titles
    titles = [
        "the Brave",
        "the Bold",
        "the Fearless",
        "the Mighty",
        "the Wise",
        "the Swift",
        "the Valiant",
        "the Conqueror",
        "the Explorer",
        "the Heroic"
    ]

    # Randomly select a title and append it to the player's name
    title = random.choice(titles)
    full_name = f"{name} {title}"

    starting_room = rooms["verdant_vestibule"]
    dex, int, wis = init_player_stats()
    player = Player(full_name, dex, int, wis, 0, 1, starting_room)
    starting_room.set_player(player)
    return player


# Game logic functions

def handle_user_input(player, boss_room, total_items):
    """
    Handle user input for player actions.

    Parameters:
    player (Player): The player object.
    boss_room (Room): The boss room object.
    total_items (int): Total number of items in the game.

    Returns:
    bool: True if easy mode is activated, False otherwise.
    """
    action = input("What would you like to do? ").strip().lower()
    if action in ["north", "south", "east", "west"]:
        player.move(action)
    elif action == "get":
        pickup_item(player)
    elif action == "exit":
        print("Exiting game. Goodbye!")
        exit()
    elif action == "e":
        print(f"\n{c.BU}Easy mode activated.{c.END} Use {c.UL}arrow keys{c.END} or {c.UL}w/a/s/d{c.END} to move, {c.UL}esc{c.END} to exit.")
        print(f'\nYou are still in the {player.current_room.name}, {player.current_room.desc}..')
        handle_easy_mode_input(player, boss_room, total_items)
        return True
    elif action == "info":
        print(player)
    elif action == "help":
        print("Available commands: 'north', 'south', 'east', 'west', 'get', 'exit', 'info', 'help', 'e' (easy mode)")
    else:
        print("Invalid command. Please enter 'north', 'south', 'east', 'west', 'get', 'exit', 'info', 'help', or 'e'.")
    return False


def handle_easy_mode_input(player, boss_room, total_items):
    no_items_message_printed = False
    last_room = player.current_room
    help_message_printed = False

    def print_room_info():
        nonlocal no_items_message_printed
        print(f'You enter the {player.current_room.name}, {player.current_room.desc}..')
        items = player.current_room.get_items()
        if items:
            print(f'\nItems in this room: {items}\n')
            for item in items:
                player.add_item(item)
                print(f"You picked up the {c.UL + item.name + c.END}.")
            no_items_message_printed = False  # Reset the flag when items are picked up
        else:
            if not no_items_message_printed:
                print("There are no items in this room.\n")
                no_items_message_printed = True  # Set the flag to prevent repeated messages

    def check_boss_room():
        if player.current_room == boss_room:
            if len(player.items) < total_items:
                print("You have entered the boss room without all the items and are too weak. Game Over!\n")
            else:
                print("Congratulations! You have defeated the Ancient Golum. You win!\n")
            return True
        return False

    while True:
        moved = False
        if keyboard.is_pressed('up') or keyboard.is_pressed('w'):
            player.move('north')
            moved = True
        elif keyboard.is_pressed('down') or keyboard.is_pressed('s'):
            player.move('south')
            moved = True
        elif keyboard.is_pressed('left') or keyboard.is_pressed('a'):
            player.move('west')
            moved = True
        elif keyboard.is_pressed('right') or keyboard.is_pressed('d'):
            player.move('east')
            moved = True
        elif keyboard.is_pressed('esc'):
            print("Exiting easy mode. Goodbye!")
            exit()
        elif keyboard.is_pressed('i'):
            print(player)
        elif keyboard.is_pressed('h') and not help_message_printed:
            print("Available commands: arrow keys or w/a/s/d to move, 'i' for info, 'h' for help, 'esc' to exit.")
            help_message_printed = True

        if moved or player.current_room != last_room:
            last_room = player.current_room
            help_message_printed = False  # Reset the flag when the player moves to a new room
            print_room_info()

            if check_boss_room():
                break

        # Add a small delay to prevent infinite loop
        time.sleep(0.1)


def pickup_item(player):
    """
    Handle item pickup based on user input.

    Parameters:
    player (Player): The player object.

    Returns:
    None
    """
    room = player.current_room
    items = room.get_items()

    if not items:
        print(f"{c.UL}There are no items in this room.{c.END}")
        return

    print(f"\n{c.UL}Items in this room:{c.END}")
    for item in items:
        print(item)

    item_name = input("Which item would you like to pick up? ").strip().lower()
    for item in items:
        if item_name == item.name.lower():
            player.add_item(item)
            print(f"\nYou picked up the {c.UL + item.name + c.END}.")
            return

    print("That item is not in this room.")


def main():
    while True:
        # Initialize game state
        rooms, items, player, boss_room, total_items = initialize_game()

        # Print welcome message
        print_welcome_message(player)

        # Initialize game loop
        logging.debug("Starting game loop")
        game_over = False
        while not game_over:
            print_current_room(player)

            # Handle player input
            if handle_user_input(player, boss_room, total_items):
                break

            # Check if player is in the boss room without all items
            if player.current_room == boss_room and len(player.items) < total_items:
                print("\nYou have entered the boss room without collecting all the items, and were eaten! Game Over!")
                game_over = True

        # Ask the player if they want to play again
        if not ask_play_again():
            print("Thank you for playing! Goodbye!")
            break


def initialize_game():
    rooms = init_rooms()
    init_room_connections(rooms)
    items = init_items()
    init_room_items(rooms, items)
    player = init_player(rooms)
    boss_room = rooms["guardians_chamber"]
    total_items = len(items)
    return rooms, items, player, boss_room, total_items


def print_welcome_message(player):
    print(f"\nWelcome {c.BU + player.name + c.END}! You find yourself in a mysterious land filled with "
          f"magic and danger.")
    print(f"{c.BOLD}Your goal is to explore the world, discover its secrets, and grow in power and wisdom.{c.END}\n")
    print("Use the commands 'north', 'south', 'east', and 'west' to move between rooms.")
    print("Use the command 'get' to pick up items in a room.")
    print("Use the command 'info' to view your character stats.")
    print("Use the command 'help' to see a list of available commands.")
    print("Use the command 'exit' to end the game.\n")
    print("Press 'e' to enable easy mode (arrow keys or w/a/s/d to move, esc to exit).\n")


def print_current_room(player):
    if not player.current_room.get_items():
        print(f'You are in the {c.BOLD + player.current_room.name + c.END}, {player.current_room.desc}')
        print("There are no items in this room.")
    else:
        print(f'\nYou are in the {player.current_room}')
        print(f'Items in this room: {player.current_room.get_items()[0]}')


def ask_play_again():
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    return play_again == 'yes'


if __name__ == "__main__":
    main()
