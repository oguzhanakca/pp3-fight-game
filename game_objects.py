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
        return 15 if self.armor == "None" else 15+self.armor.health
    def evasion(self):
        return 0 if self.armor == "None" else self.armor.evasion
    def defence(self):
        return 0 if self.armor == "None" else self.armor.defence
    
    def view_stats(self):
        weapon_name = "None" if self.weapon == "None" else self.weapon.name
        armor_name = 'None' if self.armor == 'None' else self.armor.name
        print(f"Weapon : {weapon_name}\nArmor : {armor_name}")
        print(f"Your Maximum Health : {self.health()}\nYour Damage : {self.damage()} - {self.damage()+2}\nYour Defence : {self.defence()}\nYour Critical Rate : {self.crit_rate()} %\nYour Evasion : {self.evasion()} %")



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
    def __init__(self,name,damage,defence,health,evasion,crit_rate,gold_drop):
        self.name = name
        self.damage = damage
        self.defence = defence
        self.health = health
        self.evasion = evasion
        self.crit_rate = crit_rate
        self.gold_drop = gold_drop

class PlayerCombat:
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
        self.cooldown = False
        

class EnemyCombat:
    """
    The class of enemy for combat
    """
    def __init__(self,name,damage,defence,health,evasion,crit_rate,gold_drop):
        self.name = name
        self.damage = damage
        self.defence = defence
        self.health = health
        self.evasion = evasion
        self.crit_rate = crit_rate
        self.gold_drop = gold_drop
        self.stunned = False
        

class Combat:
    """
    The class that handles combat
    """
    def attack(self,attacker,defender):
        """
        Handles attack action
        """
        evasion_roll = random.randint(0,99)<defender.evasion
        if evasion_roll: print(f"{defender.name} dodged attack.")
        else:
            damage = random.randint(attacker.damage,attacker.damage+2)-defender.defence
            if damage <= 0:
                print(f"{attacker.name} dealt no damage to {defender.name}. {defender.name} defence is too strong!")
            else:
                crit_roll = random.randint(0,99)<attacker.crit_rate
                if crit_roll:
                    damage *= 2
                    print(f"{attacker.name} dealt critical {damage} damage to {defender.name}!")
                else:
                    print(f"{attacker.name} dealt {damage} damage to {defender.name}!")
                
                defender.health -= damage
                if hasattr(attacker,"cooldown"):
                    print("Class have cooldown attribute")
                    attacker.cooldown = False
                else:
                    print("Class doesnt have cooldown attribute")

    def special_attack(self,attacker,defender):
        """
        Handles special attack action
        """
        if attacker.cooldown:
            print("Your special attack is not ready!")
        else:
            evasion_roll = random.randint(0,99)<defender.evasion
            if evasion_roll: print(f"{defender.name} dodged the special attack.")
            else:
                damage = random.randint(attacker.damage,attacker.damage+2)-defender.defence
                if damage <= 0:
                    print(f"{attacker.name} dealt no damage to {defender.name}. {defender.name} defence is too strong!")
                else:
                    crit_roll = random.randint(0,99)<attacker.crit_rate
                    if crit_roll:
                        damage *= 4
                        print(f"{attacker.name} dealt critical {damage} damage to {defender.name}!")
                    else:
                        print(f"{attacker.name} dealt {damage} damage to {defender.name}!")
                    defender.health -= damage
                    attacker.cooldown = True
                    defender.stunned = True

    def heal(self,enemy_combat,enemy):
        max_health = enemy.health
        heal_amount = enemy.damage*2
        enemy_combat.health += heal_amount
        if enemy_combat.health > max_health: enemy_combat.health = max_health
        print(f"{enemy.name} healed by {heal_amount}")
    
    def check_combat(self,player,player_combat,enemy_combat):
        """
        Checks if combat still continues
        """
        player_dead = player_combat.health <=0
        enemy_dead = enemy_combat.health <=0
        combat_end = player_dead or enemy_dead
        if combat_end:
            if player_dead: print(f"You have been killed by {enemy_combat.name}")
            if enemy_dead:
                earned_gold = random.randint(enemy_combat.gold_drop-2,enemy_combat.gold_drop+2)
                player.gold += earned_gold
                print(f"You have killed {enemy_combat.name}")
                print(f"You have earned {earned_gold} gold.")
        return combat_end


    
    