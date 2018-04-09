class Character(object):
    def __init__(self, name, description, hp, attack, defense, luck, ctype):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.type = ctype
        self.luck = luck

    def fight(self, enemy):
        enemy.hp -= self.attack

    def damage(self, enemy):
        self.hp -= enemy.attack


you = Character("Chrisopher Robin", "The child from the 100 Aker Woods", "5", "3", "3", "2", "player")
