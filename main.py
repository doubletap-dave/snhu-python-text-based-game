from dataclasses import dataclass, field
from typing import List, Optional

import logging
import random

# Configure logging
logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s [%(levelname)s] %(message)s')


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
    UNDERLINE = "\033[4m"
    BU = "\033[1m\033[4m"
    END = "\033[0m"


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
        return self.dex, self.int, self.wis # TODO: Make pretty print


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
            f"\n{Color.BU + self.name + Color.END}, "
            f"{Color.BOLD + 'Lvl' + Color.END}: {Color.CYAN + str(self.level) + Color.END}"
            f" {Color.BOLD + 'Exp' + Color.END}: {Color.GREEN + str(self.exp) + Color.END}\n"
            f" {Color.BOLD + 'Backpack' + Color.END}: {self.items}\n"
            f" {Color.BOLD + 'Dex' + Color.END}: {Color.YELLOW + str(self.dex) + Color.END}\n"
            f" {Color.BOLD + 'Int' + Color.END}: {Color.BLUE + str(self.int) + Color.END}\n"
            f" {Color.BOLD + 'Wis' + Color.END}: {Color.PURPLE + str(self.wis) + Color.END}"
        )

    def __repr__(self):
        return self.__str__()

    def add_item(self, item):
        self.items.append(item)
        self.current_room.remove_item(item)
        self.add_experience(item.exp)

    def add_experience(self, exp):
        self.exp += exp
        logging.debug(f"Player {self.name} gained {exp} experience points.")
        if self.exp >= self.exp_to_lvl_up:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_lvl_up
        logging.debug(f"Player {self.name} leveled up to level {self.level}!")


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
        return f"{self.name}: '{self.desc}'"

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
    verdant_vestibule = Room("Verdant Vestibule", "A lush garden with a fountain and blooming flowers.")
    whispering_willows = Room("Whispering Willows", "A grove of ancient trees with leaves that whisper secrets.")
    mosaic_menagerie = Room("Mosaic Menagerie", "A room filled with colorful mosaics depicting fantastical creatures.")
    guardians_chamber = Room("Guardians Chamber", "A massive stone golem stands watch over a glowing artifact.")
    runic_rotunda = Room("Runic Rotunda", "A circular chamber with glowing runes etched into the walls.")
    forgotten_fountain = Room("Forgotten Fountain", "A tranquil pool surrounded by statues of ancient heroes.")
    sunken_sanctuary = Room("Sunken Sanctuary", "An underwater grotto with shimmering fish and coral.")
    overgrown_observatory = Room("Overgrown Observatory", "A tower with a telescope that peers into the stars.")
    echoing_arboretum = Room("Echoing Arboretum", "A vast hall filled with the sound of rustling leaves.")

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
            desc="A slender flute that plays haunting melodies when the wind blows.",
            dex=2,
            int=0,
            wis=0,
            exp=10,
        ),
        "prismatic_lens": Item(
            name="Prismatic Lens",
            desc="A multifaceted lens that refracts light into a dazzling rainbow.",
            dex=0,
            int=2,
            wis=0,
            exp=10,
        ),
        "magical_stylus": Item(
            name="Magical Stylus",
            desc="A silver stylus that draws glowing runes in the air when used.",
            dex=0,
            int=0,
            wis=2,
            exp=10,
        ),
        "vial_of_glowing_water": Item(
            name="Vial of Glowing Water",
            desc="A glass vial filled with water that glows with an inner light.",
            dex=1,
            int=1,
            wis=1,
            exp=10,
        ),
        "weathered_stone_tablet": Item(
            name="Weathered Stone Tablet",
            desc="A stone tablet etched with ancient runes and symbols.",
            dex=1,
            int=1,
            wis=1,
            exp=10,
        ),
        "celestial_map": Item(
            name="Celestial Map",
            desc="A map of the stars that reveals hidden constellations.",
            dex=1,
            int=1,
            wis=1,
            exp=10,
        ),
        "resonance_crystal": Item(
            name="Resonance Crystal",
            desc="A crystal that hums with a mysterious energy when touched.",
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
    # name = input("Hail Adventurer! Please enter your name: ")
    name = "Donald J. Trump"
    starting_room = rooms["verdant_vestibule"]
    dex, int, wis = init_player_stats()
    player1 = Player(name, dex, int, wis, 0, 1, starting_room)
    starting_room.set_player(player1)
    return player1


def main():
    # initialize rooms, items, and player
    rooms = init_rooms()
    init_room_connections(rooms)

    items = init_items()
    init_room_items(rooms, items)

    player = init_player(rooms)

    # Test player/room/item interactions
    logging.debug(player.current_room)
    logging.debug(f'Available connections: {player.current_room.get_connections()}')
    logging.debug(f'Items in room: {player.current_room.get_items()}')
    player.move("east")
    logging.debug(player.current_room)
    logging.debug(f'Available connections: {player.current_room.get_connections()}')
    logging.debug(f'Items in room: {player.current_room.get_items()}')
    player.add_item(player.current_room.get_items()[0])
    logging.debug(f'Items in room: {player.current_room.get_items()}')
    player.move("east")
    logging.debug(player.current_room)
    logging.debug(f'Available connections: {player.current_room.get_connections()}')
    logging.debug(f'Items in room: {player.current_room.get_items()}')
    player.add_item(player.current_room.get_items()[0])
    print(player)


if __name__ == "__main__":
    main()
