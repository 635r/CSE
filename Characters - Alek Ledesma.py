class Character(object):
    def __init__(self, name, description, hp, attack, defense, type, luck, fight):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.type = type
        self.luck = luck
        self.fight = fight

you = Character("You", "A kid in from the 100 Aker Woods", "6", "6", "6",  )

#you
#A peacelord
#Chin Chin
#Dade
#100 Aker soldier

class MPC(object):
    def __init__(self, name, description, inventory, stats, type, luck, fight):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.type = type
        self.luck = luck
        self.fight = fight
