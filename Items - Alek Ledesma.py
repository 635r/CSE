class item(object):
    def __init__(self, boost, health, weapon, key):
        self.boost = boost
        self.health = health
        self.weapon = weapon
        self.key = key

class boost(item):
    def __init__(self, hp, attack, deffense):
        self.hp = hp
        self.attack = attack
        self.deffense = deffense

class hp (boost):
    def __init__(self, turn3, turn6):
        self.turn3 = turn3
        self.turn6 = turn6

class attack (boost):
    def __init__(self, turn3, turn6):
        self.turn3 = turn3
        self.turn6 = turn6