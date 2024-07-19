class Room:
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def __str__(self):
        return f"{self.name}: '{self.desc}'"

    def __repr__(self):
        return f"{self.name}: '{self.desc}'"
