
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


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Boost(Item):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(Boost, self).__init__(name, description)
        self.increased_stat = increased_stat
        self.num_turns = num_turns
        self.increase_of_stat = increase_of_stat


class HpTurn3(Boost):
    def __init__(self):
        super(HpTurn3, self).__init__("hp 3 turn", "a hp boost that lasts for 3 turns", 'hp', 3, 2)


class HpTurn6(Boost):
    def __init__(self):
        super(HpTurn6, self).__init__("hp 6 turn", "a hp boost that lasts for 6 turns", 'hp', 6, 2)


class AttackTurn3(Boost):
    def __init__(self):
        super(AttackTurn3, self).__init__("Attack 3 turn", "attack boost that lasts for 3 turns", 'attack', 3, 2)


class AttackTurn6(Boost):
    def __init__(self):
        super(AttackTurn6, self).__init__("Attack 6 turn", "attack boost that lasts for 6 turns", 'attack', 6, 2)


class DefenseTurn3(Boost):
    def __init__(self):
        super(DefenseTurn3, self).__init__("Defense boost 3", "a defense boost that lasts for 3 turns", 'defense', 6, 2)


class DefenseTurn6(Boost):
    def __init__(self):
        super(DefenseTurn6, self).__init__("Defense boost 6", "a defense boost that lasts for 6 turns", 'defense', 6, 2)


class Heal(Item):
    def __init__(self, name, description, restore):
        super(Heal, self).__init__(name, description)
        self.restore = restore


class Hp(Heal):
    def __init__(self, restore_hp):
        self.restore_hp = restore_hp
        super(Hp, self).__init__("hp full heal", "restores all of your health", Hp)


class Defense(Heal):
    def __init__(self, restore):
        self.restore = restore
        super(Defense, self).__init__("Defense full heal", "restore all of your defense", Defense)


class Weapon(Item):
    def __init__(self, name, description, damage, uses):
        super(Weapon, self).__init__(name, description)
        self.damage = damage
        self.uses = uses


class Gun(Weapon):
    def __init__(self, name, description, capacity, durability, damage, uses):
        super(Gun, self).__init__(name, description, damage, uses)
        self.capacity = capacity
        self.durability = durability


class AR(Gun):
    def __init__(self):
        super(AR, self).__init__("AR", "best assault rifle", 25, 3, 35, 500)


class Pistol(Gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", "basic firearm", 10, 1, 10, 50)


class Revolver(Gun):
    def __init__(self):
        super(Revolver, self).__init__("Revolver", "most powerful firearm", 6, 3, 40, 100000000)


class BigStick(Weapon):
    def __init__(self):
        super(BigStick, self).__init__("Big Stick", "a melee weapon", 12, 4)


class SmallStick(Weapon):
    def __init__(self):
        super(SmallStick, self).__init__("Small Stick", "the start of your great arsenal collection ", 24, 2)


class GoodSword(Weapon):
    def __init__(self):
        super(GoodSword, self).__init__("Good Sword", "best melee weapon", 50, 10)


class BadSword(Weapon):
    def __init__(self):
        super(BadSword, self).__init__("Bad Sword", "still better than any stick", 24, 4)


class Key(Item):
    def __init__(self, unlock, name, description):
        super(Key, self).__init__(name, description)
        self.unlock = unlock


class MilSecCard(Key):
    def __init__(self):
        super(MilSecCard, self).__init__("Military Security Card", "Security card unlocks the secure base", "MilBase")


class SpecialRock(Key):
    def __init__(self):
        super(SpecialRock, self).__init__("The Special Rock", "the special rock that'll get Pooh's attention ", "Pooh")


class Character(object):
    def __init__(self, name, description, hp, attack, defense, luck, ctype):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.type = ctype
        self.luck = luck

    def fight(self, enemy):
        enemy.hp -= self.attack

    def damage(self, enemy):
        self.hp -= enemy.attack


you = Character("Christopher Robin", "The child from the 100 Aker Woods", 100, 5, 40, 50, "player")

scout = Character("Scout", "A surveyor for the US Army", 24, 10, 0, 2, "enemy")

soldier = Character("Soldier", "Proud soldier of US Army", 50, 20, 10, 3, "enemy")

turret = Character("Auto Turret", "A fully unmanned turret", 12, 13, 20, 0, "enemy")

seal6 = Character("Seal Team 6", "The best in the USA", 666, 25, 80, 7, "boss")

pooh = Character("Winnie the Pooh", "The lovable bear friend", 1, 30, 0, 0, "ally")

piglett = Character("Piglett", "your timid friend Piglett", 1, 5, 0, 100, "ally")

tigr = Character("Tigr", "The bounciest friend you'll ever know", 1, 10, 0, 50, "ally")


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
    command = input(">_ ").lower().strip()
    if command == "quit":
        print("Weiny")
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can't go that way")
    else:
        print("I don't get it")
        print(0)
