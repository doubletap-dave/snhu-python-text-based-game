from dataclasses import dataclass, field
from typing import List, Optional

import random


# Classes
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BU = '\033[1m\033[4m'
    END = '\033[0m'


@dataclass
class Item:
    name: str
    desc: str
    dex: int
    int: int
    wis: int
    exp: int

    def __str__(self):
        return f"{self.name}: '{self.desc}' >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp}"

    def __repr__(self):
        return f"{self.name}: '{self.desc}' >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp}"


@dataclass
class Player:
    name: str
    dex: int
    int: int
    wis: int
    exp: int
    level: int
    current_room: 'Room'
    items: List[Item] = field(default_factory=list)

    def move(self, direction):
        print(f"Player {self.name} attempting to move {direction}")  # Debug print
        self.current_room.move_player(direction)

    def __str__(self):
        return (f"\n{Color.BU + self.name + Color.END}, "
                f"{Color.BOLD + 'Lvl' + Color.END}: {Color.CYAN + str(self.level) + Color.END}"
                f" {Color.BOLD + 'Exp' + Color.END}: {Color.GREEN + str(self.exp) + Color.END}\n"
                f" {Color.BOLD + 'Backpack' + Color.END}: {self.items}\n"
                f" {Color.BOLD + 'Dex' + Color.END}: {Color.YELLOW + str(self.dex) + Color.END}\n"
                f" {Color.BOLD + 'Int' + Color.END}: {Color.BLUE + str(self.int) + Color.END}\n"
                f" {Color.BOLD + 'Wis' + Color.END}: {Color.PURPLE + str(self.wis) + Color.END}")

    def __repr__(self):
        return (f"\n{Color.BU + self.name + Color.END}, "
                f"{Color.BOLD + 'Lvl' + Color.END}: {Color.CYAN + str(self.level) + Color.END}"
                f" {Color.BOLD + 'Exp' + Color.END}: {Color.GREEN + str(self.exp) + Color.END}\n"
                f" {Color.BOLD + 'Backpack' + Color.END}: {self.items}\n"
                f" {Color.BOLD + 'Dex' + Color.END}: {Color.YELLOW + str(self.dex) + Color.END}\n"
                f" {Color.BOLD + 'Int' + Color.END}: {Color.BLUE + str(self.int) + Color.END}\n"
                f" {Color.BOLD + 'Wis' + Color.END}: {Color.PURPLE + str(self.wis) + Color.END}")

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_item_count(self):
        return len(self.items)

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def set_name(self, name):
        self.name = name

    def increase_stats(self, dexterity=0, intelligence=0, wisdom=0, experience=0):
        self.dex += dexterity
        self.int += intelligence
        self.wis += wisdom
        self.exp += experience

    def increase_level(self):
        self.level += 1

    def move(self, direction):
        print(f"Player {self.name} attempting to move {direction}")  # Debug print
        self.current_room.move_player(direction)


@dataclass
class Room:
    name: str
    desc: str
    n_to: Optional['Room'] = None
    s_to: Optional['Room'] = None
    e_to: Optional['Room'] = None
    w_to: Optional['Room'] = None
    items: List[Item] = field(default_factory=list)
    player: Optional[Player] = None

    def __str__(self):
        return f"{self.name}: '{self.desc}'"

    def __repr__(self):
        return f"{self.name}: '{self.desc}'"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def get_room(self):
        return self

    def get_room_name(self):
        return self.name

    def set_player(self, player):
        self.player = player

    def get_player(self):
        return self.player

    def get_room_desc(self):
        return self.desc

    def get_connections(self):
        connections = []
        if self.n_to is not None:
            connections.append("north")
        if self.s_to is not None:
            connections.append("south")
        if self.e_to is not None:
            connections.append("east")
        if self.w_to is not None:
            connections.append("west")
        return connections

    def has_connection(self, direction):
        if direction == 'north' and self.n_to:
            return True
        elif direction == 'south' and self.s_to:
            return True
        elif direction == 'east' and self.e_to:
            return True
        elif direction == 'west' and self.w_to:
            return True
        return False

    def move_player(self, direction):
        if self.player is None:
            print("No player in the room to move.")
            return

        print(f"Attempting to move player {self.player.name} to the {direction}")  # Debug print
        connections = self.get_connections()
        if direction in connections:
            if direction == 'north' and self.n_to:
                self.n_to.set_player(self.player)
                self.player.current_room = self.n_to
            elif direction == 'south' and self.s_to:
                self.s_to.set_player(self.player)
                self.player.current_room = self.s_to
            elif direction == 'east' and self.e_to:
                self.e_to.set_player(self.player)
                self.player.current_room = self.e_to
            elif direction == 'west' and self.w_to:
                self.w_to.set_player(self.player)
                self.player.current_room = self.w_to
            print(f"Player moved to {self.player.current_room.name}")  # Debug print
            self.set_player(None)
        else:
            print("You can't go that way.")


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
    rooms["whispering_willows"].e_to = rooms["mosaic_menagerie"]
    rooms["whispering_willows"].s_to = rooms["verdant_vestibule"]

    rooms["mosaic_menagerie"].e_to = rooms["guardians_chamber"]
    rooms["mosaic_menagerie"].s_to = rooms["runic_rotunda"]
    rooms["mosaic_menagerie"].w_to = rooms["whispering_willows"]

    rooms["guardians_chamber"].w_to = rooms["mosaic_menagerie"]

    rooms["verdant_vestibule"].n_to = rooms["whispering_willows"]
    rooms["verdant_vestibule"].e_to = rooms["runic_rotunda"]
    rooms["verdant_vestibule"].s_to = rooms["sunken_sanctuary"]

    rooms["runic_rotunda"].n_to = rooms["mosaic_menagerie"]
    rooms["runic_rotunda"].e_to = rooms["forgotten_fountain"]
    rooms["runic_rotunda"].w_to = rooms["verdant_vestibule"]
    rooms["runic_rotunda"].s_to = rooms["overgrown_observatory"]

    rooms["forgotten_fountain"].w_to = rooms["runic_rotunda"]
    rooms["forgotten_fountain"].s_to = rooms["echoing_arboretum"]

    rooms["sunken_sanctuary"].n_to = rooms["verdant_vestibule"]
    rooms["sunken_sanctuary"].e_to = rooms["overgrown_observatory"]

    rooms["overgrown_observatory"].w_to = rooms["sunken_sanctuary"]
    rooms["overgrown_observatory"].n_to = rooms["runic_rotunda"]
    rooms["overgrown_observatory"].e_to = rooms["echoing_arboretum"]

    rooms["echoing_arboretum"].w_to = rooms["overgrown_observatory"]
    rooms["echoing_arboretum"].n_to = rooms["forgotten_fountain"]


def init_items():
    items = {
        "enchanted_flute": Item("Enchanted Flute", "A slender flute that plays haunting melodies when the wind blows.", 2, 0, 0, 10),
        "prismatic_lens": Item("Prismatic Lens", "A multifaceted lens that refracts light into a dazzling rainbow.", 0, 2, 0, 10),
        "magical_stylus": Item("Magical Stylus", "A silver stylus that draws glowing runes in the air when used.", 0, 0, 2, 10),
        "vial_of_glowing_water": Item("Vial of Glowing Water", "A glass vial filled with water that glows with an inner light.", 1, 1, 1, 10),
        "weathered_stone_tablet": Item("Weathered Stone Tablet", "A stone tablet etched with ancient runes and symbols.", 1, 1, 1, 10),
        "celestial_map": Item("Celestial Map", "A map of the stars that reveals hidden constellations.", 1, 1, 1, 10),
        "resonance_crystal": Item("Resonance Crystal", "A crystal that hums with a mysterious energy when touched.", 1, 1, 1, 10),
    }
    return items


def init_room_items(rooms, items):
    rooms["whispering_willows"].add_item(items["enchanted_flute"])
    rooms["mosaic_menagerie"].add_item(items["prismatic_lens"])
    rooms["runic_rotunda"].add_item(items["magical_stylus"])
    rooms["forgotten_fountain"].add_item(items["vial_of_glowing_water"])
    rooms["sunken_sanctuary"].add_item(items["weathered_stone_tablet"])
    rooms["overgrown_observatory"].add_item(items["celestial_map"])
    rooms['echoing_arboretum'].add_item(items['resonance_crystal'])


def init_player_stats():
    dex = random.randint(1, 10)
    int = random.randint(1, 10)
    wis = random.randint(1, 10)
    return dex, int, wis


def init_player(rooms):
    starting_room = rooms["verdant_vestibule"]
    dex, int, wis = init_player_stats()
    player1 = Player("Donald Trump", dex, int, wis, 0, 1, starting_room)
    starting_room.set_player(player1)
    return player1


def main():
    rooms = init_rooms()
    init_room_connections(rooms)
    items = init_items()
    init_room_items(rooms, items)
    player = init_player(rooms)
    print(player)

    starting_room = rooms["verdant_vestibule"]
    print(f"\nConnections from {starting_room.name}: {starting_room.get_connections()}")
    if starting_room.get_player() is not None:
        print(f"\nPlayer in starting room: {starting_room.get_player().name}")  # Debug print
    else:
        print("\nNo player in the starting room.")  # Debug print

    player.move('north')
    print(player.current_room.get_items())


if __name__ == "__main__":
    main()
