class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Boost(Item):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(Boost, self).__init__()
        self.description = description
        self.name = name
        self.increased_stat = increased_stat
        self.num_turns = num_turns
        self.increase_of_stat = increase_of_stat


class hp_turn3 (Boost):
    def __init__(self):
        super(hp_turn3, self).__init__("hp 3 turn", "a hp boost that lasts for 3 turns", hp, 3, 2)

class HpTurn6 (Boost):
    def __init__(self):
        super(HpTurn6, self).__init__("hp 6 turn", "a hp boost that lasts for 6 turns", hp, 6, 2)


class AttackTurn3(Boost):
    def __init__(self):
        super(AttackTurn3, self).__init__("Attack 3 turn", "attack boost that lasts for 3 turns", attack, 3, 2)

class AttackTurn6 (Boost):
    def __init__(self):
        super(AttackTurn6, self).__init__("Attack 6 turn", "attack boost that lasts for 6 turns", attack, 6, 2)



class DefenseTurn3 (Boost):
    def __init__(self):
        super(DefenseTurn3, self).__init__("Defense boost 3", "a defense boost that lasts for 3 turns", defense, 6, 2)


class DefenseTurn6 (Boost):
    def __init__(self):
        super(DefenseTurn6, self).__init__("Defense boost 6", "a defense boost that lasts for 6 turns", defense, 6, 2)



class heal (Item):
    def __init__(self, name, description, restore):
        super(heal, self).__init__()

class hp (heal):
    def __init__(self, restore_hp):
        self.restore_hp = restore_hp
        super(hp, self).__init__("hp full heal", "restores all of your health", hp)

class defense (heal):
    def __init__(self, restore):
        self.restore = restore
        super(defense, self).__init__("Defense full heal", "restore all of your defense", defense)


class weapon (Item):
    def __init__(self, name, description, damage, uses):
        self.description = description
        self.name = name
        self.damage = damage
        self.uses = uses

class gun (weapon):
    def __init__(self, name, description, capacity, durability, damage, uses):
        super(gun, self).__init__()
        self.description = description
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.damage = damage
        self.uses = uses

    
class AR (gun):
    def __init__(self):
        super(AR, self).__init__("AR", "best assault rifle", 25, 3, 35, 500)

class Pistol (gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", "basic firearm", 10, 1, 10, 50)

class Revolver (gun):
    def __init__(self):
        super(Revolver, self).__init__("Revolover", "most powerful firearm", 6, 3, 40, 100000000)

class big_stick (weapon):
    def __init__(self):
        super(big_stick, self).__init__("Big Stick" , "a melee weapon", 12, 4)

class small_stick (weapon):
    def __init__(self):
        super(small_stick, self).__init__("Small Stick", "the start of your great arsenal collection ", 24, 2)

class good_sword (weapon):
    def __init__(self):
        super(good_sword, self).__init__("Good Sword", "best melee weapon", 50, 10)

class bad_sword (weapon):
    def __init__(self):
        super(bad_sword, self).__init__( "Bad Sword", "still better than any stick", 24, 4)


class key (item):
    def __init__(self, unlock):
        self.unlock = unlock
        super(key, self).__init__()
        
class mil_sec_card (key):
    def __init__(self):
        super(mil_sec_card, self).__init__(mil_base)

class special_rock (key):
    def __init__(self):
        super(special_rock, self).__init__(poohs house)

