import room


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
        return f"{self.name} >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp} - LVL: {self.level} - ITEMS: {self.items}"

    def __repr__(self):
        return f"{self.name} >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp} - LVL: {self.level} - ITEMS: {self.items}"

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

    def increase_stats(self, dexterity=0, intelligence=0, wisdom=0, experience=0):
        self.dex += dexterity
        self.int += intelligence
        self.wis += wisdom
        self.exp += experience

    def increase_level(self):
        self.level += 1

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