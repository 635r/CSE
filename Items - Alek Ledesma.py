class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class boost(item):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description)
        self.increase_stat = increase_stat

class hp_turn3 (boost):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)

class hp_turn6 (boost):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)


class attack_turn3(boost):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)

class attack_turn6 (boost):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)


class defense (boost):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)


class defense_turn3 (boost):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)


class defence_turn6 (boost):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)


class heal (item):
    def __init__(self, name, description, increase_stat):
        super(boost, self).__init__(name, description, increase_stat)


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
        super(AR, self).__init__(25, 3)

class Pistol (gun):
    def __init__(self):
        super(Pistol, self).__init__(10, 1)

class Revolver (gun):
    def __init__(self):
        super(Revolver, self).__init__(6, 3)


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

