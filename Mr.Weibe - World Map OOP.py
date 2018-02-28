class Room(object):
    def __init__(self, name, north, south, east, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


home = Room("Home", 'north_home', None, )
west_home = Room("West of Home", "west_home")
north_home = Room("North of Home", None)
east_home = Room("East of Home", )
south_home = Room("South of Home",)
