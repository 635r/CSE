
class Room(object):
    def __init__(self, name, north, south, east, west, description, enemy_in_room):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.enemy_in_room = enemy_in_room

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Character(object):
    def __init__(self, name, description, hp, attack, defense, luck, c_type, max_hp, inventory):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.c_type = c_type
        self.luck = luck
        self.max_hp = max_hp
        self.inventory = inventory

    def fight(self, enemy):
        enemy.hp -= self.attack

    def damage(self, enemy):
        self.hp -= enemy.attack - self.defense


your_inv = {}


def ded(you):
        if you.hp <= 0 or you.hp == 0:
            print("oof, you ded")
            quit(0)


none = Character("none", "none", 0, 0, 0, 0, "none", 0, "nothing")

you = Character("Christopher Robin", "The child from the 100 Aker Woods", 100, 5, 40, 50, "player", 100, your_inv)

scout = Character("Scout", "A surveyor for the US Army", 24, 10, 0, 2, "enemy", 24, "revolver")

soldier = Character("Soldier", "Proud soldier of US Army", 50, 20, 10, 3, "enemy", 50, "AR")

turret = Character("Auto Turret", "A fully unmanned turret", 12, 13, 20, 0, "enemy", 12, "Pistol")

seal6 = Character("Seal Team 6", "The best in the USA", 666, 25, 80, 7, "boss", 666, "SCAR")

pooh = Character("Winnie the Pooh", "The lovable bear friend", 1, 30, 0, 0, "ally", 1, "GreatSword")

piglett = Character("Piglett", "your timid friend Piglett", 1, 5, 0, 100, "ally", 1, "BigStick")

tigr = Character("Tigr", "The bounciest friend you'll ever know", 1, 10, 0, 50, "ally", 1, "BigStick")

heffalump = Character("Heffalump", "A bonus round", 900, 20, 2, 0, "boss", 4000, "SCAR")


Home = Room("Home", "NorthHome", "SouthHome", "EastHome", "WestHome",
            "All the other places are East of the house", none)

SouthHome = Room("South of Home", "Home", "Eeyore", None, "Owl",
                 "Owl sits inside, You wave but he's busy reading", none)

EastHome = Room("East of Home", None, None, None, "Home", "the East edge of the map", none)

NorthHome = Room("North of Home", "NPole", "Home", None, "RabbitFamRange",
                 "To the North are a Bee Tree and the North Pole", none)

WestHome = Room("West of Home", "North Pole", "Owl", "Home", "NE100Aker", "west of the home", none)

Owl = Room("Owl's Home", "NPole", "Eeyore", "Home", "NE100Aker",
           "Owl is high up in the trees too absorbed in his bokk to pay any mind to you", soldier)

Eeyore = Room("Eeyore Home", "Home", None, None, "MilBase",
              "The place is sad and depressing, Eeyore is asleep in his house of sticks", soldier)

RabbitFamRange = Room("Rabbit's Family Range", None, "NW100Aker", "Home", "Rabbit",
                      "Rabbit apears to have quite the the family tree",soldier)

Rabbit = Room("Rabbit's House", "The Sandy Pit Roo Plays in", "NW100Aker", "RabbitFamRange",
              "Kanga's house", "Rabbit is outside tending to his garden right outside of his burrow", soldier)

NE100Aker = Room("NE 100 Aker Woods", "RabbitFamRange", "MilBase", "Owl",
                 "North 100 Aker Woods", "You're gonna need a key card to get in", soldier)

NW100Aker = Room("NW 100 Aker Woods", "Rabbit", "SW100Aker", "NE100Aker", "Pine",
                 "Must be called 100 akers for a reason", soldier)

SW100Aker = Room("SW 100 Aker Woods", "NE100Aker", None, "MilBase", "Where the Woozle Wasn't",
                 "These woods must be like 100 Akers", soldier)

MilBase = Room("The Military Base", "NE100Aker", None, "Eeyore", "SW100Aker",
               "Looks like a Military base. You should check it out once you have a Security Card", seal6)

Pooh = Room("Pooh Bear's Home", None, "Piglett", "Pine", None,
            "It looks like Pooh went out to the Bee Tree", soldier)

WoozleWasnt = Room("Where the Woozle wasn't", "Pine", "Floody", "SW100Aker", piglett,
                   "You notice a distinct lack Woozle", soldier)

Floody = Room("Floody Place", "Piglett", None, "Eeyore", None,
              "This place floods every now and then during the floody season", scout)

Pine = Room("6 Pine Forest", "Kanga", "WoozleWasnt", "NW100Aker", "Pooh",
            "There are 6 pine trees and the trap for the heffalump", heffalump)

Piglett = Room("Piglett's Home", "Pooh", "Floody PLace", "6 Pine Trees", None,
               "It would appear that Piglett is out and about with Pooh", soldier)

PicnicArea = Room("PicnicArea", None, "SandPit", None, None, "A great place to have a picnic", scout)

Kanga = Room("Kanga", "PicnicArea", "Pine", "Rabbit", None,
             "The house where Kanga and Roo live", soldier)

SandPit = Room("SandPit", "PicnicArea", "Rabbit", "RabbitFamRange",
               "Kanga's House", "Looks like Roo isn't here but at home with Kanga", scout)

NPole = Room("NPole", None, "Home", None, "BeeTree",
             "The farthest North this game allows you to go", scout)

BeeTree = Room("BeeTree", None, "Home", "Owl", "PicnicArea",
               "There are Pooh and Piglett collecting honey", "none")


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

    def boost_hp3(self, player):
        player.hp += self.increase_of_stat


class HpTurn6(Boost):
    def __init__(self):
        super(HpTurn6, self).__init__("hp 6 turn", "a hp boost that lasts for 6 turns", 'hp', 6, 2)

    def boost_hp6(self, player):
        player.hp += self.increase_of_stat


class AttackTurn3(Boost):
    def __init__(self):
        super(AttackTurn3, self).__init__("Attack 3 turn", "attack boost that lasts for 3 turns", 'attack', 3, 2)

    def boost_attack3(self, player):
        player.attack += self.increase_of_stat


class AttackTurn6(Boost):
    def __init__(self):
        super(AttackTurn6, self).__init__("Attack 6 turn", "attack boost that lasts for 6 turns", 'attack', 6, 2)

    def boost_attack6(self, player):
        player.attack += self.increase_of_stat


class DefenseTurn3(Boost):
    def __init__(self):
        super(DefenseTurn3, self).__init__("Defense boost 3", "a defense boost that lasts for 3 turns", 'defense', 6, 2)

    def boost_defense3(self, player):
        player.defense += self.increase_of_stat


class DefenseTurn6(Boost):
    def __init__(self):
        super(DefenseTurn6, self).__init__("Defense boost 6", "a defense boost that lasts for 6 turns", 'defense', 6, 2)

    def boost_defense6(self, player):
        player.defense += self.increase_of_stat


class Heal(Item):
    def __init__(self, name, description, restore):
        super(Heal, self).__init__(name, description)
        self.restore = restore


class Hp(Heal):
    def __init__(self, restore_hp):
        self.restore_hp = restore_hp
        super(Hp, self).__init__("hp full heal", "restores all of your health", Hp)

    def potion(self):
        you.hp = you.max_hp


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

    def shoot(self, enemy):
        enemy.hp -= you.attack


class Pistol(Gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", "basic firearm", 10, 1, 10, 50)

    def shoot(self, enemy):
        enemy.hp -= you.attack


class Revolver(Gun):
    def __init__(self):
        super(Revolver, self).__init__("Revolver", "most powerful firearm", 6, 3, 40, 100000000)

    def shoot(self, enemy):
        enemy.hp -= you.attack


class BigStick(Weapon):
    def __init__(self):
        super(BigStick, self).__init__("Big Stick", "a melee weapon", 12, 4)

    def poke(self, enemy, BigStick):
        enemy.hp -= BigStick.damage


class SmallStick(Weapon):
    def __init__(self):
        super(SmallStick, self).__init__("Small Stick", "the start of your great arsenal collection ", 24, 2)

    def poke(self, enemy):
        enemy.hp -= you.attack


class GoodSword(Weapon):
    def __init__(self):
        super(GoodSword, self).__init__("Good Sword", "best melee weapon", 50, 10)

    def slash(self, enemy):
        enemy.hp -= you.attack


class BadSword(Weapon):
    def __init__(self):
        super(BadSword, self).__init__("Bad Sword", "still better than any stick", 24, 4)

    def slash(self, enemy):
        enemy.hp -= you.attack


class Key(Item):
    def __init__(self, unlock, name, description):
        super(Key, self).__init__(name, description)
        self.unlock = unlock


class MilSecCard(Key):
    def __init__(self):
        super(MilSecCard, self).__init__("MilBase", "Security card unlocks the secure base", "Military Security Card")

    def unlock(self, MilBase):
        MilBase.locked = MilBase.woke


class SpecialRock(Key):
    def __init__(self):
        super(SpecialRock, self).__init__("Pooh", "The Special Rock", "the special rock that'll get Pooh's attention ")

    def unlock(self, Pooh):
        Pooh.locked = Pooh.woke


class Nothing(Item):
    def __init__(self):
        super(Nothing, self).__init__("nothing", "nothing here to fight")

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


def encounter(
    print("%s has set his sights on you" ),
    print("______________________________________"),
    print("will you?"),
    print("1 Fight "
          "2 Heal "
          "3 Boost")
    if input(1)
        print("______________________________________")
        print("with what weapon?"),

        if input(weapon)
            

)