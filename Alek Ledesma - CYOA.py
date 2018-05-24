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
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(HpTurn3, self).__init__(name, description, increased_stat, num_turns, increase_of_stat)

    def boost_hp3(self, player):
        player.hp += self.increase_of_stat


class HpTurn6(Boost):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(HpTurn6, self).__init__(name, description, increased_stat, num_turns, increase_of_stat)

    def boost_hp6(self, player):
        player.hp += self.increase_of_stat


class AttackTurn3(Boost):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(AttackTurn3, self).__init__(name, description, increased_stat, num_turns, increase_of_stat)

    def boost_attack3(self, player):
        player.attack += self.increase_of_stat


class AttackTurn6(Boost):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(AttackTurn6, self).__init__(name, description, increased_stat, num_turns, increase_of_stat)

    def boost_attack6(self, player):
        player.attack += self.increase_of_stat


class DefenseTurn3(Boost):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(DefenseTurn3, self).__init__(name, description, increased_stat, num_turns, increase_of_stat)

    def boost_defense3(self, player):
        player.defense += self.increase_of_stat


class DefenseTurn6(Boost):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(DefenseTurn6, self).__init__(name, description, increased_stat, num_turns, increase_of_stat)

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
        Player.hp = Player.max_hp


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


class Ar(Gun):
    def __init__(self, name, description, capacity, durability, damage, uses):
        super(Ar, self).__init__(name, description, capacity, durability, damage, uses)

    def shoot(self, enemy):
        enemy.hp -= Player.attack


class Pist(Gun):
    def __init__(self, name, description, capacity, durability, damage, uses):
        super(Pist, self).__init__(name, description, capacity, durability, damage, uses)

    def shoot(self, enemy):
        enemy.hp -= Player.attack


class Rev(Gun):
    def __init__(self, name, description, capacity, durability, damage, uses):
        super(Rev, self).__init__(name, description, capacity, durability, damage, uses)

    def shoot(self, enemy):
        enemy.hp -= Player.attack


class BS(Weapon):
    def __init__(self, name, description, damage, uses):
        super(BS, self).__init__(name, description, damage, uses)

    def poke(self, enemy, BS):
        enemy.hp -= BS.damage


class SS(Weapon):
    def __init__(self, name, description, damage, uses):
        super(SS, self).__init__(name, description, damage, uses)

    def poke(self, enemy):
        enemy.hp -= Player.attack


class GSwrd(Weapon):
    def __init__(self, name, description, damage, uses):
        super(GSwrd, self).__init__(name, description, damage, uses)

    def slash(self, enemy):
        enemy.hp -= Player.attack


class BSwrd(Weapon):
    def __init__(self, name, description, damage, uses):
        super(BSwrd, self).__init__(name, description, damage, uses)

    def slash(self, enemy):
        enemy.hp -= Player.attack


class Key(Item):
    def __init__(self, unlock, name, description):
        super(Key, self).__init__(name, description)
        self.unlock = unlock


class MilSecCrd(Key):
    def __init__(self):
        super(MilSecCrd, self).__init__("MilBase", "Security card unlocks the secure base",
                                        "Military Security Card")

    def unlock(self, MilBase):
        MilBase.locked = MilBase.woke


class SpecialRock(Key):
    def __init__(self):
        super(SpecialRock, self).__init__("Pooh", "The Special Rock",
                                          "the special rock that'll get Pooh's attention ")

    def unlock(self, Pooh):
        Pooh.locked = Pooh.woke


class Nothing(Item):
    def __init__(self):
        super(Nothing, self).__init__("nothing", "nothing here to fight")


class Character(object):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.max_hp = max_hp
        self.inventory = inventory

    def fight(self, enemy):
        enemy.hp -= self.attack

    def damage(self, enemy):
        self.hp -= enemy.attack - self.defense


class Enemy(Character):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
            super(Enemy, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)

    your_inv = {}


def ded(you):
        if you.hp <= 0 or you.hp == 0:
            print("oof, you ded")
            quit(0)


class Player(Character):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Player, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Scout(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Scout, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Soldier1(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Soldier1, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Turret(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Turret, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Seal6(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Seal6, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Pooh(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Pooh, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Piglett(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Piglett, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Tigr(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Tigr, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


class Heffalump(Enemy):
    def __init__(self, name, description, hp, attack, defense, luck, max_hp, inventory):
        super(Heffalump, self).__init__(name, description, hp, attack, defense, luck, max_hp, inventory)


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


AR = Ar("AR", "best assault rifle", 25, 3, 35, 500)

Pistol = Pist("Pistol", "basic firearm", 10, 1, 10, 50)

Revolver = Rev("Revolver", "most powerful firearm", 6, 3, 40, 100000000)

GoodSword = GSwrd("Good Sword", "best melee weapon", 50, 10)

BadSword = BSwrd("Bad Sword", "still better than any stick", 24, 4)

BigStick = BS("Big Stick", "a melee weapon", 12, 4)

SmallStick = SS("Small Stick", "the start of your great arsenal collection ", 24, 2)


HP3 = HpTurn3("hp 3 turn", "a hp boost that lasts for 3 turns", 'hp', 3, 2)

HP6 = HpTurn6("hp 6 turn", "a hp boost that lasts for 6 turns", 'hp', 6, 2)

ATCK3 = AttackTurn3("Attack 3 turn", "attack boost that lasts for 3 turns", 'attack', 3, 2)

ATCK6 = AttackTurn6("Attack 6 turn", "attack boost that lasts for 6 turns", 'attack', 6, 2)

DEF3 = DefenseTurn3("Defense boost 3", "a defense boost that lasts for 3 turns", 'defense', 3, 2)

DEF6 = DefenseTurn6("Defense boost 6", "a defense boost that lasts for 6 turns", 'defense', 6, 2)


Player = Player("Christopher Robin", "The child from the 100 Aker Woods", 100, 5, 40, 50, 100, [])

Scout = Scout("Scout", "A surveyor for the US Army", 24, 10, 0, 2, 24, Revolver)

Soldier = Soldier1("Soldier", "Proud soldier of US Army", 50, 20, 10, 3, 50, AR)

Turret = Turret("Auto Turret", "A fully unmanned turret", 12, 13, 20, 0, 12, Pistol)

Seal6 = Seal6("Seal Team 6", "The best in the USA", 666, 25, 80, 7, 666, AR)

Pooh = Pooh("Winnie the Pooh", "The lovable bear friend", 1, 30, 0, 0, 1, GoodSword)

Piglett = Piglett("Piglett", "your timid friend Piglett", 1, 5, 0, 100, 1, BigStick)

Tigr = Tigr("Tigr", "The bounciest friend you'll ever know", 1, 10, 0, 50, 1, BigStick)

Heffalump = Heffalump("Heffalump", "A bonus round", 900, 20, 2, 0, 4000, AR)


Home = Room("Home", "NorthHome", "SouthHome", "EastHome", "WestHome",
            "All the other places are East of the house", None)

SouthHome = Room("South of Home", "Home", "Eeyore", None, "Owl",
                 "Owl sits inside, You wave but he's busy reading", None)

EastHome = Room("East of Home", None, None, None, "Home", "the East edge of the map", None)

NorthHome = Room("North of Home", "NPole", "Home", None, "RabbitFamRange",
                 "To the North are a Bee Tree and the North Pole", None)

WestHome = Room("West of Home", "North Pole", "Owl", "Home", "NE100Aker", "west of the home", None)

Owl = Room("Owl's Home", "NPole", "Eeyore", "Home", "NE100Aker",
           "Owl is high up in the trees too absorbed in his bokk to pay any mind to you", Soldier)

Eeyore = Room("Eeyore Home", "Home", None, None, "MilBase",
              "The place is sad and depressing, Eeyore is asleep in his house of sticks", Soldier)

RabbitFamRange = Room("Rabbit's Family Range", None, "NW100Aker", "Home", "Rabbit",
                      "Rabbit apears to have quite the the family tree", Soldier)

Rabbit = Room("Rabbit's House", "The Sandy Pit Roo Plays in", "NW100Aker", "RabbitFamRange",
              "Kanga's house", "Rabbit is outside tending to his garden right outside of his burrow", Soldier)

NE100Aker = Room("NE 100 Aker Woods", "RabbitFamRange", "MilBase", "Owl",
                 "North 100 Aker Woods", "You're gonna need a key card to get in", Soldier)

NW100Aker = Room("NW 100 Aker Woods", "Rabbit", "SW100Aker", "NE100Aker", "Pine",
                 "Must be called 100 akers for a reason", Soldier)

SW100Aker = Room("SW 100 Aker Woods", "NE100Aker", None, "MilBase", "Where the Woozle Wasn't",
                 "These woods must be like 100 Akers", Soldier)

MilBase = Room("The Military Base", "NE100Aker", None, "Eeyore", "SW100Aker",
               "Looks like a Military base. You should check it out once you have a Security Card", Seal6)

pooh = Room("Pooh Bear's Home", None, "Piglett", "Pine", None,
            "It looks like Pooh went out to the Bee Tree", Soldier1)

WoozleWasnt = Room("Where the Woozle wasn't", "Pine", "Floody", "SW100Aker", Piglett,
                   "You notice a distinct lack Woozle", Soldier1)

Floody = Room("Floody Place", "Piglett", None, "Eeyore", None,
              "This place floods every now and then during the floody season", Scout)

Pine = Room("6 Pine Forest", "Kanga", "WoozleWasnt", "NW100Aker", "Pooh",
            "There are 6 pine trees and the trap for the heffalump", Heffalump)

piglett = Room("Piglett's Home", "Pooh", "Floody PLace", "6 Pine Trees", None,
               "It would appear that Piglett is out and about with Pooh", Soldier)

PicnicArea = Room("PicnicArea", None, "SandPit", None, None, "A great place to have a picnic", Scout)

Kanga = Room("Kanga", "PicnicArea", "Pine", "Rabbit", None,
             "The house where Kanga and Roo live", Soldier)

SandPit = Room("SandPit", "PicnicArea", "Rabbit", "RabbitFamRange",
               "Kanga's House", "Looks like Roo isn't here but at home with Kanga", Scout)

NPole = Room("NPole", None, "Home", None, "BeeTree",
             "The farthest North this game allows you to go", Scout)

BeeTree = Room("BeeTree", None, "Home", "Owl", "PicnicArea",
               "There are Pooh and Piglett collecting honey", "None")


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

    if current_node.enemy_in_room is not None:
        print("%s has set his sights on you" % current_node.enemy_in_room.name)
        print("______________________________________")
        print("What will you do?")
        print("1 Fight\n2 Heal\n3 Boost")
        if command == 1:
            print("You died")
        if command == 2:
            print("You died")
        if command == 3:
            print("You died")
        print("%s has set his sights on you" % current_node.enemy_in_room.name)
        print(current_node.enemy_in_room.description)

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
