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


class HpTurn6 (Boost):
    def __init__(self):
        super(HpTurn6, self).__init__("hp 6 turn", "a hp boost that lasts for 6 turns", 'hp', 6, 2)


class AttackTurn3(Boost):
    def __init__(self):
        super(AttackTurn3, self).__init__("Attack 3 turn", "attack boost that lasts for 3 turns", 'attack', 3, 2)


class AttackTurn6 (Boost):
    def __init__(self):
        super(AttackTurn6, self).__init__("Attack 6 turn", "attack boost that lasts for 6 turns", 'attack', 6, 2)


class DefenseTurn3 (Boost):
    def __init__(self):
        super(DefenseTurn3, self).__init__("Defense boost 3", "a defense boost that lasts for 3 turns", 'defense', 6, 2)


class DefenseTurn6 (Boost):
    def __init__(self):
        super(DefenseTurn6, self).__init__("Defense boost 6", "a defense boost that lasts for 6 turns", 'defense', 6, 2)


class Heal(Item):
    def __init__(self, name, description, restore):
        super(Heal, self).__init__(name, description)
        self.restore = restore


class Hp (Heal):
    def __init__(self, restore_hp):
        self.restore_hp = restore_hp
        super(Hp, self).__init__("hp full heal", "restores all of your health", Hp)


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

    
class AR (Gun):
    def __init__(self):
        super(AR, self).__init__("AR", "best assault rifle", 25, 3, 35, 500)


class Pistol (Gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", "basic firearm", 10, 1, 10, 50)


class Revolver (Gun):
    def __init__(self):
        super(Revolver, self).__init__("Revolver", "most powerful firearm", 6, 3, 40, 100000000)


class BigStick (Weapon):
    def __init__(self):
        super(BigStick, self).__init__("Big Stick", "a melee weapon", 12, 4)


class SmallStick (Weapon):
    def __init__(self):
        super(SmallStick, self).__init__("Small Stick", "the start of your great arsenal collection ", 24, 2)


class GoodSword (Weapon):
    def __init__(self):
        super(GoodSword, self).__init__("Good Sword", "best melee weapon", 50, 10)


class BadSword (Weapon):
    def __init__(self):
        super(BadSword, self).__init__("Bad Sword", "still better than any stick", 24, 4)


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

