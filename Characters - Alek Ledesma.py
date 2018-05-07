class Character(object):
    def __init__(self, name, description, hp, attack, defense, luck, ctype, max_hp, inventory):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.ctype = ctype
        self.luck = luck
        self.max_hp = max_hp
        self.inventory = inventory

    def fight(self, enemy):
        enemy.hp -= self.attack

    def damage(self, enemy):
        self.hp -= enemy.attack - self.defense

your_inv = {}

you = Character("Christopher Robin", "The child from the 100 Aker Woods", 100, 5, 40, 50, "player", 100, your_inv)

scout = Character("Scout", "A surveyor for the US Army", 24, 10, 0, 2, "enemy", 24, your_inv)

soldier = Character("Soldier", "Proud soldier of US Army", 50, 20, 10, 3, "enemy", 50, your_inv)

turret = Character("Auto Turret", "A fully unmanned turret", 12, 13, 20, 0, "enemy", 12, your_inv)

seal6 = Character("Seal Team 6", "The best in the USA", 666, 25, 80, 7, "boss", 666, your_inv)

pooh = Character("Winnie the Pooh", "The lovable bear friend", 1, 30, 0, 0, "ally", 1, your_inv)

piglett = Character("Piglett", "your timid friend Piglett", 1, 5, 0, 100, "ally", 1, your_inv)

tigr = Character("Tigr", "The bounciest friend you'll ever know", 1, 10, 0, 50, "ally", 1, your_inv)



