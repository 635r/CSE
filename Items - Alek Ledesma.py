class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class boost(item):
    def __init__(self, increase_stat):
        super(boost, self).__init__()
        self.increase_stat = increase_stat

class hp (boost):
    def __init__(self):
        super(hp, self).__init__(hp)

class hp_turn3 ():
    def __init__(self):
        super(hp_turn3, self).__init__()

class hp_turn6 ():
    def __init__(self):
        super(hp_turn6, self).__init__()
class attack (boost):
    def __init__(self):
        super(attack, self).__init__(attack)

class attack_turn3():
    def __init__(self):
        super().__init__()

class attack_turn6 ():
    def __init__(self):
        super().__init__()

class defense (boost):
    def __init__(self):


class defense_turn3 ():
    def __init__(self):

class defence_turn6 ():
    def __init__(self):


class heal (item):
    def __init__(self, restore_stat):
        self.restore_stat

class hp (heal):
    def __init__(self, restore_hp):
        self.restore_hp

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
        super(AR, self).__init__(6, 25, 3)

class Pistol (gun):
    def __init__(self):
        super(Pistol, self).__init__(10, 1)

class Revolver (gun)


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

