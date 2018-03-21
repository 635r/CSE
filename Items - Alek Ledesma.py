class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class boost(item):
    def __init__(self, increase_stat):
        super(boost, self).__init__(self.increase_stat)
        self.increase_stat = increase_stat

class hp (boost):
    def __init__(self):
        super(hp, self).__init__(hp)

class hp_turn3 ():
    def __init__(self):

class hp_turn6 ():
    def __init__(self):

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
    def __init__(self, turn3, turn6):
        self.turn3 = turn3
        self.turn6 = turn6


class heal (item):
    def __init__(self, hp, defense):
        self.hp = hp
        self.defense = defense

class hp (heal):
    def __init__(self, ten, fifteen):
        self.ten = ten
        self.fifteen = fifteen

class defense (heal):
    def __init__(self, restore):
        self.restore = restore


class weapon (item):
    def __init__(self, damage, uses):
        self.damage = damage
        self.uses = uses

class gun (weapon):
    def __init__(self, capacity):
        self.capacity = capacity

class AR (gun):
    def __init__(self):
        super(AR, self).__init__(0)


class sword (weapon):
    def __init__(self, good, bad):
        self.good = good
        self.bad = bad

class stick (weapon):
    def __init__(self, big, small):
        self.big = big
        self.small = small


class key (item):
    def __init__(self, unlock):
        self.unlock = unlock

