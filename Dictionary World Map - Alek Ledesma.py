world_map = {
    "HOME": {
        "NAME": "HOME",
        "DESCRIPTION": "All of your friend's houses lie east of your home(which is were you are)",
        "PATHS": {
            "NORTH": "NORTH_HOUSE",
            "SOUTH": "SOUTH_HOUSE",
            "EAST": "EAST_HOUSE",
            "WEST": "WEST_HOUSE",
         }
    },
    "SOUTH_HOME": {
        "NAME": "South of Home",
        "DESCRIPTION": "To the South are OWL'S HOUSE, EEYORES'S HOUSE",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "EAST_HOME": {
        "NAME": "East of Home",
        "DESCRIPTION": "This is as far East as you want to go",
        "PATHS": {
            "NORTH": None,
            "SOUTH": None,
            "EAST": None,
            "WEST": "HOME",
         }
    },
    "NORTH_HOME": {
        "NAME": "North of Home",
        "DESCRIPTION": "To the North are a bunch of BIG ROCKS, a BEE TREE, and the NORTHPOLE",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "WEST_HOME": {
        "NAME": "West of Home",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "OWL": {
        "NAME": "Owl's house",
        "DESCRIPTION": "high up in the trees, you see Owl reading. You wave, but he's to caught up in it",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "EEYORE": {
        "NAME":"Eeyore's house",
        "DESCRIPTION": "It's a sad little place. You see Eeyore asleep in his stick tent",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "Rabbit_FamRange": {
        "NAME": "Rabbit's Family Range",
        "DESCRIPTION": "Rabbit appears to have quite the family tree",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "RABBIT": {
        "NAME": "Rabbit's house",
        "DESCRIPTION": "You see Rabbit tending to his garden. It's right outside of his burrow",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "100AKER": {
        "NAME": "100 Aker Woods",
        "DESCRIPTION": "These woods could be like 100 ackers long",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "POOH": {
        "NAME": "Pooh Bear's house",
        "DESCRIPTION": "It would apear that Pooh has already gone to the BEE TREE",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "WOOZLE_WASNT": {
        "NAME": "Where the Woozle Wasn't",
        "DESCRIPTION": "You notice a distinct lack of Woozle",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "FLOODY": {
        "NAME": "Floody Place",
        "DESCRIPTION": "This place floods every now and then during the floody season",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "6PINES": {
        "NAME": "6 Pine Trees",
        "DESCRIPTION": "You see 6 pine trees a trap for a the Heffalump",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "PIGLETT": {
        "NAME": "Piglett's house",
        "DESCRIPTION": "Looks like Piglett went out with Pooh",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "PICNIC_AREA": {
        "NAME": "Picnic Area",
        "DESCRIPTION": "Looks like a great place for a picnic. Maybe you'll comeback with some friends",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "KANGA": {
        "NAME": "Kanga's House",
        "DESCRIPTION": "You see Kanga tending to Roo. You wave and Kanga waves back",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "SAND_PIT": {
        "NAME": "The Sandy Pit that Roo Plays in",
        "DESCRIPTION": "Seems like Roo is at home with Kanga",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
         }
    },
    "MIL_BASE": {
        "NAME": "A Military Base",
        "DESCRIPTION": "Looks like some kind of base. You should probably go now",
        "PATHS": {
            "NORTH": "100AKER",
            "SOUTH": "100AKER",
            "EAST": "EEYORE",
            "WEST": "",
         }
    }
}

current_node = world_map["HOME"]
directions = ["NORTH", "SOUTH", "EAST", "WEST"]

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input (">_ ")
    if command == "quit":
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node["PATHS"][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You can't go that way")
    else:
        print("I don't get it")
        print(0)
