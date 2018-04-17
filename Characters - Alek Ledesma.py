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


you = Character("Chrisopher Robin", "The child from the 100 Aker Woods", 100, 5, 40, 50, "player")
scout = Character("Scout", "A serveyor for the US Army", 24, 10, 0, 2, "enemy")
soldier = Character("Soldier", "Proud soldier of US Army", 50, 20, 10, 3, "enemy")
turret = Character("Auto Turret", "A fully unmanned turret", 12, 13, 20, 0, "enemy")
seal6 = Character("Seal Team 6", "The best in the USA", 666, 69, 80, 7, "boss")
pooh = Character("Winnie the Pooh", "The lovable bear friend", 10000000, 30, 0, 7, "ally")
piglett = Character("Piglett", "your timid friend Piglett", 10000000, 5, 0, 100, "ally")

