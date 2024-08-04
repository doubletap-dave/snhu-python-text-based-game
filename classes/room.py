class Room:
    def __init__(self, name, description, north=None, south=None, east=None, west=None, items=[]):
        self.name = name
        self.desc = description
        self.n_to = north
        self.s_to = south
        self.e_to = east
        self.w_to = west
        self.items = items

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

    def get_room_desc(self):
        return self.desc

    # def get_connections(self):
    #     connections = []
    #     if self.n_to is not None:
    #         connections.append("north")
    #     if self.s_to is not None:
    #         connections.append("south")
    #     if self.e_to is not None:
    #         connections.append("east")
    #     if self.w_to is not None:
    #         connections.append("west")
    #     return connections

    # get room connections and their names
    def get_connections(self):
        connections = []
        if self.n_to is not None:
            connections.append(f"North: {self.n_to.get_room_name()}")
        if self.s_to is not None:
            connections.append(f"South: {self.s_to.get_room_name()}")
        if self.e_to is not None:
            connections.append(f"East: {self.e_to.get_room_name()}")
        if self.w_to is not None:
            connections.append(f"West: {self.w_to.get_room_name()}")
        return connections