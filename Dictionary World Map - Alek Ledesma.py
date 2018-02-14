world_map = {
    "HOME": {
        "NAME": "HOME",
        "DESCRIPTION": "All of your friend's houses lie east of your home(which is were you are)",
        "PATHS": {
            "NORTH": "NORTHHOUSE",
            "SOUTH": "SOUTHHOUSE",
            "EAST": "EASTHOUSE",
            "WEST": "WESTHOUSE",
         }
    },
    "SOUTHHOUSE": {
        "NAME": "SOUTH OF HOME",
        "DESCRIPTION": "To the South are OWL'S HOUSE, EEYORES'S HOUSE"
    },
    "EASTHOUSE": {
        "NAME": "EAST OF HOME",
        "DESCRIPTION": "This is as far East as you want to go"
    },
    "NORTHHOUSE": {
        "NAME": "NORTH OF HOME",
        "DESCRIPTION": "To the North are a bunch of BIG ROCKS, a BEE TREE, and the NORTHPOLE"
    },
    "WESTHOUSE": {
        "NAME": "WEST OF HOME",
        "DESCRIPTION": "fub"
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
            print("You can't go that way boi")
    else:
        print("I don't get it")
        print()