class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Boost(Item):
    def __init__(self, name, description, increased_stat, num_turns, increase_of_stat):
        super(Boost, self).__init__(name, description)
        self.increased_stat = increased_stat
        self.num_turns = num_turns
        self.increase_of_stat = increase_of_stat


class HpTurn3 (Boost):
    def __init__(self):
        super(HpTurn3, self).__init__("hp 3 turn", "a hp boost that lasts for 3 turns", 'hp', 3, 2)

    def boost_hp3(self, player):
        player.hp += self.increase_of_stat


class hpturn6 (Boost):
    def __init__(self):
        super(hpturn6, self).__init__("hp 6 turn", "a hp boost that lasts for 6 turns", 'hp', 6, 2)

    def boost_hp6(self, player):
        player.hp += self.increase_of_stat


class AttackTurn3(Boost):
    def __init__(self):
        super(AttackTurn3, self).__init__("Attack 3 turn", "attack boost that lasts for 3 turns", 'attack', 3, 2)

    def boost_attack3(self, player):
        player.attack += self.increase_of_stat


class AttackTurn6 (Boost):
    def __init__(self):
        super(AttackTurn6, self).__init__("Attack 6 turn", "attack boost that lasts for 6 turns", 'attack', 6, 2)

    def boost_attack6(self, player):
        player.attack += self.increase_of_stat


class DefenseTurn3 (Boost):
    def __init__(self):
        super(DefenseTurn3, self).__init__("Defense boost 3", "a defense boost that lasts for 3 turns", 'defense', 6, 2)

    def boost_defense3(self, player):
        player.defense += self.increase_of_stat


class DefenseTurn6 (Boost):
    def __init__(self):
        super(DefenseTurn6, self).__init__("Defense boost 6", "a defense boost that lasts for 6 turns", 'defense', 6, 2)

    def boost_defense6(self, player):
        player.defense += self.increase_of_stat


class Heal(Item):
    def __init__(self, name, description, restore):
        super(Heal, self).__init__(name, description)
        self.restore = restore


class Hp (Heal):
    def __init__(self, restore_hp):
        self.restore_hp = restore_hp
        super(Hp, self).__init__("hp full heal", "restores all of your health", Hp)

    def heal(self, player):
        player.hp = self.max_hp


class Defense (Heal):
    def __init__(self, restore):
        self.restore = restore
        super(Defense, self).__init__("Defense full heal", "restore all of your defense", Defense)


class Weapon (Item):
    def __init__(self, name, description, damage, uses):
        super(Weapon, self).__init__(name, description)
        self.damage = damage
        self.uses = uses


class Gun (Weapon):
    def __init__(self, name, description, capacity, durability, damage, uses):
        super(Gun, self).__init__(name, description, damage, uses)
        self.capacity = capacity
        self.durability = durability

class ar (Gun):
    def __init__(self):
        super(ar, self).__init__("AR", "best assault rifle", 25, 3, 35, 500)

    def shoot(self, ar, enemy):
        enemy.hp -= ar.damage


class pistol (Gun):
    def __init__(self):
        super(pistol, self).__init__("Pistol", "basic firearm", 10, 1, 10, 50)

    def shoot(self, pistol, enemy):
        enemy.hp -= pistol.damage


class revolver (Gun):
    def __init__(self):
        super(revolver, self).__init__("Revolver", "most powerful firearm", 6, 3, 40, 100000000)

    def shoot(self, revolver, enemy):
        enemy.hp -= revolver.damage


class bigstick (Weapon):
    def __init__(self):
        super(bigstick, self).__init__("Big Stick", "a melee weapon", 12, 4)


class smallstick (Weapon):
    def __init__(self):
        super(smallstick, self).__init__("Small Stick", "the start of your great arsenal collection ", 24, 2)


class goodsword (Weapon):
    def __init__(self):
        super(goodsword, self).__init__("Good Sword", "best melee weapon", 50, 10)


class badsword (Weapon):
    def __init__(self):
        super(badsword, self).__init__("Bad Sword", "still better than any stick", 24, 4)


class Key (Item):
    def __init__(self, unlock, name, description):
        super(Key, self).__init__(name, description)
        self.unlock = unlock

        
class MilSecCard (Key):
    def __init__(self):
        super(MilSecCard, self).__init__("Military Security Card", "Security card unlocks the secure base", "MilBase")


class SpecialRock (Key):
    def __init__(self):
        super(SpecialRock, self).__init__("The Special Rock", "the special rock that'll get Pooh's attention ", "Pooh")
