class Player:
    """
    The class that contains player data
    """
    def __init__(self,name, weapon, armor,gold):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.gold = gold


class Weapon:
    """
    The class that shows player's current weapon
    """
    def __init__(self,id,name,damage,crit_rate):
        self.id = id
        self.name = name
        self.damage = damage
        self.crit_rate = crit_rate

class Armor:
    """
    The class that shows player's current armor
    """
    def __init__(self,id,name,defence,evasion,health):
        self.id = id
        self.name = name
        self.defence = defence
        self.evasion = evasion
        self.health = health

class Enemy:
    """
    The class that contains enemy data
    """
    def __init__(self,name,defense,evasion,health,price):
        self.name = name
        self.defense = defense
        self.evasion = evasion
        self.health = health
        self.price = price

class Combat:
    """
    The class that handles combat
    """

    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy

    