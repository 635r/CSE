class item(object):
    def __init__(self, boost, heal, weapon, key):
        self.boost = boost
        self.heal = heal
        self.weapon = weapon
        self.key = key


class boost(item):
    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense

class hp (boost):
    def __init__(self, turn3, turn6):
        self.turn3 = turn3
        self.turn6 = turn6

class attack (boost):
    def __init__(self, turn3, turn6):
        self.turn3 = turn3
        self.turn6 = turn6

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
    def __init__(self, sword, gun, stick):
        self.sword = sword
        self. gun = gun
        self. stick = stick

class gun (weapon):
    def __init__(self, AR, revolver, pistol):
        self.AR = AR
        self.revolver = revolver
        self.pistol = pistol

class sword (weapon):
    def __init__(self, good, bad):
        self.good = good
        self.bad = bad

class stick (weapon):
    def __init__(self, big, small):
        self.big = big
        self.small = small


class key (item):
    def __init__(self, rock, security):
        self.rock = rock
        self.security = security