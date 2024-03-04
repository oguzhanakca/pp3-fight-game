class Player:
    """
    The class that contains player data
    """
    def __init__(self,name, health, weapon, armor,gold):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.gold = gold

class Weapon:
    """
    Player's current weapon data
    """
    def __init__(self,name,damage,crit_rate,price):
        self.name = name
        self.damage = damage
        self.crit_rate = crit_rate
        self.price = price

class Armor:
    """
    Player's current armor data
    """
    def __init__(self,name,defense,evasion,health,price):
        self.name = name
        self.defense = defense
        self.evasion = evasion
        self.health = health
        self.price = price

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