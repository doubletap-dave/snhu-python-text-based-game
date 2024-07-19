class Player:
    def __init__(self, name, dexterity, intelligence, wisdom, experience):
        self.name = name
        self.dex = dexterity
        self.int = intelligence
        self.wis = wisdom
        self.exp = experience

    def __str__(self):
        return f"{self.name} >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp}"

    def __repr__(self):
        return f"{self.name} >> DEX: {self.dex} - INT: {self.int} - WIS: {self.wis} - EXP: {self.exp}"
