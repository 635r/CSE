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


Home = Room("Home", "North of home", "South of home", "East of home", "West of home")

SouthHome = Room("South of Home", "Home", "Eeyore's House", None, "Owl's House")

EastHome = Room("East of Home", None, None, None, "Home" )

NorthHome = Room("North of Home", "Home", None, "Rabbit's Family Range")

west_home = Room("West of Home","North Pole", "Owl's Home", "Home", "NE 100 Aker Woods" )

Owl = Room("Owl's Home", "North Pole", "Eeyore", "Home", "NE 100 Aker Woods" )

Eeyore = Room("Eeyore's House", "Home", None, None, "A Military Base")

RabbitFamrange = Room("Rabbit's Family Range", None, "NW 100 Aker Woods", "Home", "Rabbit's House")

Rabbit = Room("Rabbit's House", "The Sandy Pit Roo Plays in", "NW 100 Aker woods", "Rabbit's  Family Range", "Kanga's House")

NE100Aker = Room("NE 100 Aker Woods", "Rabbit's Family Range", "A Military Base", "")
NW100Aker = Room("NW 100 Aker Woods")
SW100Aker = Room("SW 100 Aker Woods")

MilBase = Room("A Military Base", "NE 100 Aker Woods",None, "Eeyore's House", "SW 100 Aker Woods" )

Pooh = Room("Pooh Bear's House", None, "Piglett's House", "6 Pine Trees", None)

WoozleWasnt = Room("Where the Woozle Wasn't", "6 Pine Trees", "Floody Place", "SW 100 Aker Woods", "Piglett's House")

Floody = Room("Floody Place", "Piglett's House", None, "Eeyore's House", None)

Pine = Room("6 Pine Trees", "Kanga's House", "Where the Woozle Wasn't", "NW 100 Aker Woods", "Pooh Bear's House")

Piglett = Room("Piglett", "Pooh", "Floody PLace", "6 Pine Trees", None)

PicnicArea = Room("Picnic Area", None, "The Sandy Pit Roo Plays in", None, None, "A great place to have a picnic")

Kanga = Room("Kanga's House","Picnic Area", "6 Pine Trees", "Rabbit's House", None, "The house where Kanga and Roo live")

SandPit = Room("The Sandy Pit that Roo Plays in", "Picnic Area", "Rabbit's House", "Rabbit's Family Range", "Kanga's House")

NPole = Room("North Pole", None, "Home", None, "Bee Tree")

BeeTree = Room("Bee Tree", None, "Home", "Owl's House", "Picnic Area")
