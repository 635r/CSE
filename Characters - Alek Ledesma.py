class Character(object):
    def __init__(self, name, description, inventory, stats, type, luck, fight):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.type = type
        self.luck = luck
        self.fight = fight


class MPC(object):
    def __init__(self, name, description, inventory, stats, type, luck, fight):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.type = type
        self.luck = luck
        self.fight = fight
