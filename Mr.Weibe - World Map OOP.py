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


home = Room("Home", "North of home", "South of home", "East of home", "West of home")
south_home = Room("South of Home", "Home", "Eeyore's House", None, "Owl's House")
east_home = Room("East of Home", None, None, None, "Home" )
north_home = Room("North of Home", "Home", None, "Rabbit Family Range")
west_home = Room("West of Home","North Pole", "Owl's Home", "Home", "NE 100 Aker Woods" )
owl = Room("Owl's Home", "North Pole", "Eeyore", "Home", "NE 100 Aker Woods" )
eeyore = Room("EEYORE")
rabbit_famrange = Room("RABBIT_FAMRANGE")
rabbit = Room("RABBIT")
ne100aker = Room("NE100AKER")
nw100aker = Room("NW100AKER")
sw100aker = Room("SW100AKER")
mil_base = Room("MIL_BASE")
pooh = Room("POOH")
woozle_wasnt = Room("WOOZLE_WASNT")
floody = Room("FLOODY")
6pine = Room("6PINE")
piglett = Room("Piglett", "Pooh", "Floody PLace", "6 Pine Trees", None)
picnic_area =Room("PICNIC_AREA")
kanga = Room("KANGA")
sand_pit = Room("SNAD_PIT")
npole = Room("NPOLE")
bee_tree = Room("Bee Tree", None, "Home", "Owl's House", "Picnic Area")
