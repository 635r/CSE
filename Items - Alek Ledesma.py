class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self):
        print: ("what do you want to use?")

class booster(item):
    def __init__(self, increased_stat, num_turns, increase_of_stat):
        super(booster, self).__init__()
        self.increased_stat = increased_stat
        self.num_turns = num_turns
        self.increase_of_stat = increase_of_stat

    def boost(self):
        print:("which boost will you use?")

class hp_turn3 (booster):
    def __init__(self):
        super(hp_turn3, self).__init__(hp, 3, 5)

class hp_turn6 (booster):
    def __init__(self):
        super(hp_turn6, self).__init__(hp, 6, 5)


class attack_turn3 (booster):
    def __init__(self):
        super(attack_turn3).__init__(attack, 3, 5)

class attack_turn6 (booster):
    def __init__(self):
        super().__init__(attack, 6, 5)



class defense_turn3 (booster):
    def __init__(self):
        super(defense_turn3, self).__init__(defense, 3, 5)

class defense_turn6 (booster):
    def __init__(self):
        super(defense_turn6, self).__init__(defense, 6, 5)

class heal (item):
    def __init__(self, restore_stat):
        super(heal, self).__init__()
        self.restore_stat = restore_stat

class hp (heal):
    def __init__(self, restore_hp):
        self.restore_hp = restore_hp

class defense (heal):
    def __init__(self, restore):
        self.restore = restore


class weapon (item):
    def __init__(self, damage, uses):
        self.damage = damage
        self.uses = uses

class gun (weapon):
    def __init__(self, capacity, durability):
        super(gun, self).__init__()
        self.capacity = capacity
        self.durability = durability

    
class AR (gun):
    def __init__(self):
        super(AR, self).__init__(25, 5)

class Pistol (gun):
    def __init__(self):
        super(Pistol, self).__init__(10, 1)

class Revolver (gun)
    def __init__(self):
        super(Revolver, self).__init__(6, 1)

class big_stick (weapon):
    def __init__(self):
        super(big_stick, self).__init__(12, 5)

class small_stick (weapon):
    def __init__(self):
        super(small_stick, self).__init__(24, 2)

class good_sword (weapon):
    def __init__(self):
        super(good_sword, self).__init__(50, 10)

class bad_sword (weapon):
    def __init__(self):
        super(bad_sword, self).__init__(24, 4)

class key (item):
    def __init__(self, unlock):
        self.unlock = unlock
        
class mil_sec_card (key):
    def __init__(self):
        super(mil_sec_card, self).__init__(mil_base)

class special_rock (key):
    def __init__(self):
        super(special_rock, self).__init__(poohs house)

