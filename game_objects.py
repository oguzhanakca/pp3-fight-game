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