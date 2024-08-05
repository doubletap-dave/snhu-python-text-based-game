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


class Player:
    def __init__(self, name, dexterity, intelligence, wisdom, experience, level, location, items=[]):
        self.name = name
        self.dex = dexterity
        self.int = intelligence
        self.wis = wisdom
        self.exp = experience
        self.level = level
        self.location = location
        self.items = items

    def __str__(self):
        return (f"\n{Color.BU + self.name + Color.END}, "
                f"{Color.BOLD + 'Lvl' + Color.END}: {Color.CYAN + str(self.level) + Color.END}"
                f" {Color.BOLD + 'Exp' + Color.END}: {Color.GREEN + str(self.exp) + Color.END}\n"
                f" {Color.BOLD + 'Location' + Color.END}: {self.location}\n"
                f" {Color.BOLD + 'Backpack' + Color.END}: {self.items}\n"
                f" {Color.BOLD + 'Dex' + Color.END}: {Color.YELLOW + str(self.dex) + Color.END}\n"
                f" {Color.BOLD + 'Int' + Color.END}: {Color.BLUE + str(self.int) + Color.END}\n"
                f" {Color.BOLD + 'Wis' + Color.END}: {Color.PURPLE + str(self.wis) + Color.END}")

    def __repr__(self):
        return (f"\n{Color.BU + self.name + Color.END}, "
                f"{Color.BOLD + 'Lvl' + Color.END}: {Color.CYAN + str(self.level) + Color.END}"
                f" {Color.BOLD + 'Exp' + Color.END}: {Color.GREEN + str(self.exp) + Color.END}\n"
                f" {Color.BOLD + 'Location' + Color.END}: {self.location}\n"
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

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def set_name(self, name):
        self.name = name

    def increase_stats(self, dexterity=0, intelligence=0, wisdom=0, experience=0):
        self.dex += dexterity
        self.int += intelligence
        self.wis += wisdom
        self.exp += experience

    def increase_level(self):
        self.level += 1

    # TODO: Make player object aware of its location and the connections to other rooms
    def get_connections(self):
        connections = []
        if self.location.n_to is not None:
            connections.append(f"North: {self.location.n_to.get_room_name()}")
        if self.location.s_to is not None:
            connections.append(f"South: {self.location.s_to.get_room_name()}")
        if self.location.e_to is not None:
            connections.append(f"East: {self.location.e_to.get_room_name()}")
        if self.location.w_to is not None:
            connections.append(f"West: {self.location.w_to.get_room_name()}")
        return connections

    def move(self, direction):
        if direction == "n":
            self.location = self.location.n_to
        elif direction == "s":
            self.location = self.location.s_to
        elif direction == "e":
            self.location = self.location.e_to
        elif direction == "w":
            self.location = self.location.w_to
        else:
            return "Invalid direction. Please try again."
