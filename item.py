class Item:
    def __init__(self, name, description, dexterity, intelligence, wisdom, experience):
        self.name = name
        self.desc = description
        self.dex = dexterity
        self.int = intelligence
        self.wis = wisdom
        self.exp = experience

    def __str__(self):
        return f"{self.name}: '{self.desc}' >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp}"

    def __repr__(self):
        return f"{self.name}: '{self.desc}' >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp}"
