class Room(object):
    def __init__(self, name, description, north, south, east, west):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


Home = Room("Home", "North of home", "South of home", "East of home", "West of home",
            "All the other places are East of the house")

SouthHome = Room("South of Home", "Home", "Eeyore's House", None, "Owl's House",
                 "Owl sits inside, You wave but he's busy reading")

EastHome = Room("East of Home", None, None, None, "Home", "the East edge of the map")

NorthHome = Room("North of Home", "North Pole", "Home", None, "Rabbit's Family Range",
                 "To the North are a Bee Tree and the North Pole")

west_home = Room("West of Home", "North Pole", "Owl's Home", "Home", "NE 100 Aker Woods", "west of the home")

Owl = Room("Owl's Home", "North Pole", "Eeyore", "Home", "NE 100 Aker Woods",
           "Owl is high up in the trees too absorbed in his bokk to pay any mind to you")

Eeyore = Room("Eeyore's House", "Home", None, None, "A Military Base",
              "The place is sad and depressing, Eeyore is asleep in his house of sticks")

RabbitFamRange = Room("Rabbit's Family Range", None, "NW 100 Aker Woods", "Home", "Rabbit's House",
                      "Rabbit apears to have quite the the family tree")

Rabbit = Room("Rabbit's House", "The Sandy Pit Roo Plays in", "NW 100 Aker woods", "Rabbit's  Family Range",
              "Kanga's house", "Rabbit is outside tending to his garden right outside of his burrow")

NE100Aker = Room("NE 100 Aker Woods", "Rabbit's Family Range", "A Military Base", "Owl's House",
                 "North 100 Aker Woods", "You're gonna need a key card to get in")

NW100Aker = Room("NW 100 Aker Woods", "Rabbit's House", "SW 100 Aker Woods", "NE 100 Aker Woods", "6 Pine Trees",
                 "Must be called 100 akers for a reason")
SW100Aker = Room("SW 100 Aker Woods", "NE 100 Aker Woods", None, "Military Base", "Where the Woozle Wasn't",
                 "These woods must be like 100 akers")

MilBase = Room("A Military Base", "NE 100 Aker Woods", None, "Eeyore's House", "SW 100 Aker Woods",
               "Looks like a Military base. You should check it out once you have a Security Card")

Pooh = Room("Pooh Bear's House", None, "Piglett's House", "6 Pine Trees", None,
            "It looks like Pooh went out to the Bee Tree")

WoozleWasnt = Room("Where the Woozle Wasn't", "6 Pine Trees", "Floody Place", "SW 100 Aker Woods", "Piglett's House",
                   "You notice a distinct lack Woozle")

Floody = Room("Floody Place", "Piglett's House", None, "Eeyore's House", None,
              "This place floods every now and then during the floody season")

Pine = Room("6 Pine Trees", "Kanga's House", "Where the Woozle Wasn't", "NW 100 Aker Woods", "Pooh Bear's House",
            "There are 6 pine trees and the trap for the heffalump")

Piglett = Room("Piglett", "Pooh", "Floody PLace", "6 Pine Trees", None,
               "It would apear that Piglett is out and about with Pooh")

PicnicArea = Room("Picnic Area", None, "The Sandy Pit Roo Plays in", None, None, "A great place to have a picnic")

Kanga = Room("Kanga's House", "Picnic Area", "6 Pine Trees", "Rabbit's House", None,
             "The house where Kanga and Roo live")

SandPit = Room("The Sandy Pit that Roo Plays in", "Picnic Area", "Rabbit's House", "Rabbit's Family Range",
               "Kanga's House", "Looks like Roo isn't here but at home with Kanga")

NPole = Room("North Pole", None, "Home", None, "Bee Tree",
             "The farthest North this game allows you to go")

BeeTree = Room("Bee Tree", None, "Home", "Owl's House", "Picnic Area",
               "There are Pooh and Piglett collecting honey")

current_node = Home
directions = ["north", "south", "east", "west"]
short_directions = ["n", "s", "e", "w"]

while True:
    print(current_node.name)
    print(current_node.description)
    command = input (">_ ").lower().strip()
    if command == "quit":
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try: current_node.move(command)
        except KeyError:
            print("You can't go that way")
    else:
        print("I don't get it")
        print(0)