import random
class Player:
    """
    The class that contains player data
    """
    def __init__(self,name, weapon, armor,gold):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.gold = gold

class Stats:
    """
    Contains final player stats from weapon and armor
    """
    def __init__(self,weapon,armor):
        self.weapon = weapon
        self.armor = armor

    def damage(self):
        return 1 if self.weapon == "None" else 1+self.weapon.damage
    def crit_rate(self):
        return 0 if self.weapon == "None" else self.weapon.crit_rate
    def health(self):
        return 10 if self.armor == "None" else 10+self.armor.health
    def evasion(self):
        return 0 if self.armor == "None" else self.armor.evasion
    def defence(self):
        return 0 if self.armor == "None" else self.armor.defence
    
    def view_stats(self):
        print(f"Weapon : {self.weapon.name}\nArmor : {self.armor.name}")
        print(f"Your Maximum Health : {self.health()}\nYour Damage : {self.damage()}\nYour Defence : {self.defence()}\nYour Critical Rate : {self.crit_rate()}%\nYour Evasion : {self.evasion()}%")



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
    def __init__(self,name,damage,defense,health,gold_drop):
        self.name = name
        self.damage = damage
        self.defense = defense
        self.health = health
        self.gold_drop = gold_drop

class Player_Combat:
    """
    The class of player for combat
    """
    def __init__(self,name,damage,crit_rate,health,evasion,defence):
        self.name = name
        self.damage = damage
        self.crit_rate = crit_rate
        self.health = health
        self.evasion = evasion
        self.defence = defence
        

class Enemy_Combat:
    """
    The class of enemy for combat
    """
    def __init__(self,name,damage,defence,health,evasion,crit_rate,drop):
        self.name = name
        self.damage = damage
        self.defence = defence
        self.health = health
        self.evasion = evasion
        self.crit_rate = crit_rate
        self.drop = drop
        

class Combat:
    """
    The class that handles combat
    """

    def attack(attacker,defender):
        evasion_roll = random.randint(0,100)<defender.evasion
        if evasion_roll: print(f"{defender.name} dodged attack.")
        else:
            damage = attacker.damage-defender.defence
            if damage <= 0:
                print(f"{attacker.name} dealt no damage to {defender.name}. {defender.name} defence is too strong!")
            else:
                crit_roll = random.randint(0,100)<attacker.crit_rate
                if crit_roll:
                    damage *= 2
                print(f"{attacker.name} dealt critical {damage} damage to {defender.name}!")
            defender.health -= damage


    
    