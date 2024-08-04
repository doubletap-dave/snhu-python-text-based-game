import room


class Player:
    def __init__(self, name, dexterity, intelligence, wisdom, experience, level, items=[]):
        self.name = name
        self.dex = dexterity
        self.int = intelligence
        self.wis = wisdom
        self.exp = experience
        self.level = level
        self.items = items

    def __str__(self):
        return f"{self.name} >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp} - LVL: {self.level} - ITEMS: {self.items}"

    def __repr__(self):
        return f"{self.name} >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp} - LVL: {self.level} - ITEMS: {self.items}"

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def increase_stats(self, dexterity=0, intelligence=0, wisdom=0, experience=0):
        self.dex += dexterity
        self.int += intelligence
        self.wis += wisdom
        self.exp += experience

    def increase_level(self):
        self.level += 1

    def move(self, direction):
        if direction == "n":
            return room.Room.get_room(self.n_to)
        elif direction == "s":
            return room.Room.get_room(self.s_to)
        elif direction == "e":
            return room.Room.get_room(self.e_to)
        elif direction == "w":
            return room.Room.get_room(self.w_to)
        else:
            return "Invalid direction. Please try again."
