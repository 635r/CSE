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

north_home = Room("North of Home", "Home", None, "Rabbit's Family Range")

west_home = Room("West of Home","North Pole", "Owl's Home", "Home", "NE 100 Aker Woods" )

owl = Room("Owl's Home", "North Pole", "Eeyore", "Home", "NE 100 Aker Woods" )

eeyore = Room("Eeyore's House", "Home", None, None, "A Military Base")

rabbit_famrange = Room("Rabbit's Family Range", None, "NW 100 Aker Woods", "Home", "Rabbit's House")

rabbit = Room("Rabbit's House", "The Sandy Pit Roo Plays in", "NW 100 Aker woods", "Rabbit's  Family Range", "Kanga's House")

ne100aker = Room("NE 100 Aker Woods")
nw100aker = Room("NW 100 Aker Woods")
sw100aker = Room("SW 100 Aker Woods")

mil_base = Room("A Military Base", "NE 100 Aker Woods",None, "Eeyore's House", "SW 100 Aker Woods" )

pooh = Room("Pooh Bear's House", None, "Piglett's House", "6 Pine Trees", None)

woozle_wasnt = Room("Where the Woozle Wasn't", "6 Pine Trees", "Floody Place", "SW 100 Aker Woods", "Piglett's House")

floody = Room("Floody Place", "Piglett's House", None, "Eeyore's House", None)

6pine = Room("6 Pine Trees", "Kanga's House", "Where the Woozle Wasn't", "NW 100 Aker Woods", "Pooh Bear's House")

piglett = Room("Piglett", "Pooh", "Floody PLace", "6 Pine Trees", None)

picnic_area =Room("Picnic Area", None, "The Sandy Pit Roo Plays in", None, None)

kanga = Room("Kanga's House","Picnic Area", "6 Pine Trees", "Rabbit's House", None )

sand_pit = Room("The Sandy Pit that Roo Plays in", "Picnic Area", "Rabbit's House", "Rabbit's Family Range", "Kanga's House")

npole = Room("North Pole", None, "Home", None, "Bee Tree")

bee_tree = Room("Bee Tree", None, "Home", "Owl's House", "Picnic Area")
