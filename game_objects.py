import random
from colorama import Fore


class Player:
    """
    The class that contains player data
    """
    def __init__(self, name, weapon, armor, gold, feedback_sent):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.gold = gold
        self.feedback_sent = feedback_sent


class Stats:
    """
    Contains final player stats from weapon and armor
    """
    def __init__(self, weapon, armor):
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
        print(Fore.MAGENTA)
        print(f"Weapon : {weapon_name}\nArmor : {armor_name}")
        print(Fore.RESET)
        print(Fore.YELLOW)
        print(f"Your Maximum Health : {self.health()}")
        print(f"Your Damage : {self.damage()} - {self.damage()+2}")
        print(f"Your Defence : {self.defence()}")
        print(f"Your Critical Rate : {self.crit_rate()} %")
        print(f"Your Evasion : {self.evasion()} %")
        print(Fore.RESET)


class Weapon:
    """
    The class that shows player's current weapon
    """
    def __init__(self, id, name, damage, crit_rate):
        self.id = id
        self.name = name
        self.damage = damage
        self.crit_rate = crit_rate


class Armor:
    """
    The class that shows player's current armor
    """
    def __init__(self, id, name, defence, evasion, health):
        self.id = id
        self.name = name
        self.defence = defence
        self.evasion = evasion
        self.health = health


class Enemy:
    """
    The class that contains enemy data
    """
    def __init__(self, name, dmg, defence, hp, eva, crit_rate, drop):
        self.name = name
        self.dmg = dmg
        self.defence = defence
        self.hp = hp
        self.eva = eva
        self.crit_rate = crit_rate
        self.drop = drop


class PlayerCombat:
    """
    The class of player for combat
    """
    def __init__(self, name, dmg, crit_rate, hp, evasion, defence):
        self.name = name
        self.dmg = dmg
        self.crit_rate = crit_rate
        self.hp = hp
        self.evasion = evasion
        self.defence = defence
        self.cooldown = False


class EnemyCombat:
    """
    The class of enemy for combat
    """
    def __init__(self, name, dmg, defence, hp, evasion, rate, drop):
        self.name = name
        self.dmg = dmg
        self.defence = defence
        self.hp = hp
        self.evasion = evasion
        self.rate = rate
        self.drop = drop
        self.stunned = False


class Combat:
    """
    The class that handles combat
    a = attacker
    d = defender
    """
    def attack(self, a, d):
        """
        Handles attack action
        """
        evasion_roll = random.randint(0, 99) < d.evasion
        if evasion_roll:
            print(Fore.LIGHTGREEN_EX)
            print(f"{d.name} dodged attack.")
            print(Fore.RESET)
        else:
            damage = random.randint(a.dmg, a.dmg+2)-d.defence
            if damage <= 0:
                print(Fore.LIGHTYELLOW_EX)
                print(f"{d.name} blocked all damage.")
                print(Fore.RESET)
            else:
                crit_roll = random.randint(0, 99) < a.crit_rate
                if crit_roll:
                    damage *= 2
                    print(Fore.RED)
                    print(f"{a.name} dealt critical {damage} damage.")
                    print(Fore.RESET)
                else:
                    print(Fore.RED)
                    print(f"{a.name} dealt {damage} damage.")
                    print(Fore.RESET)
                d.hp -= damage
                if hasattr(a, "cooldown"):
                    a.cooldown = False

    def special_attack(self, a, d):
        """
        Handles special attack action
        """
        if a.cooldown:
            print(Fore.MAGENTA)
            print("Your special attack is not ready!")
            print(Fore.RESET)
        else:
            evasion_roll = random.randint(0, 99) < d.evasion
            if evasion_roll:
                print(Fore.LIGHTGREEN_EX)
                print(f"{d.name} dodged the special attack.")
                print(Fore.RESET)
            else:
                damage = random.randint(a.dmg, a.dmg+2)-d.defence
                if damage <= 0:
                    print(Fore.LIGHTYELLOW_EX)
                    print(f"{d.name} blocked all damage.")
                    print(Fore.RESET)
                else:
                    crit_roll = random.randint(0, 99) < a.crit_rate
                    if crit_roll:
                        damage *= 4
                        print(Fore.RED)
                        print(f"{a.name} dealt critical {damage} damage.")
                        print(Fore.RESET)
                    else:
                        print(Fore.LIGHTRED_EX)
                        print(f"{a.name} dealt {damage} damage.")
                        print(Fore.RESET)
                    d.hp -= damage
                    a.cooldown = True
                    d.stunned = True

    def heal(self, enemy_combat, enemy):
        max_health = enemy.hp
        heal_amount = int(max_health/2)
        enemy_combat.hp += heal_amount
        if enemy_combat.hp > max_health:
            enemy_combat.hp = max_health
        print(Fore.GREEN)
        print(f"{enemy.name} healed by {heal_amount}")
        print(Fore.RESET)

    def check_combat(self, player, player_combat, enemy_combat):
        """
        Checks if combat still continues
        """
        player_dead = player_combat.hp <= 0
        enemy_dead = enemy_combat.hp <= 0
        combat_end = player_dead or enemy_dead
        if combat_end:
            if player_dead:
                print(Fore.MAGENTA)
                print(f"You have been killed by {enemy_combat.name}")
                print(Fore.RESET)
                gold_lost = enemy_combat.drop*4
                player.gold -= gold_lost
                if player.gold < 0:
                    player.gold = 0
                print(Fore.YELLOW + f"You lost {gold_lost} gold." + Fore.RESET)
                return "defeated"
            if enemy_dead:
                print(f"You have killed {enemy_combat.name}")
                if enemy_combat.name == "Demon King":
                    print(Fore.GREEN)
                    print("Congratulations !\nYou beat the game.")
                    print(Fore.RESET)
                    return "finished"
                else:
                    drop = enemy_combat.drop
                    earned_gold = random.randint(drop-2, drop+2)
                    player.gold += earned_gold
                    print(Fore.YELLOW)
                    print(f"You have earned {earned_gold} gold.")
                    print(Fore.RESET)
                    return "killed"
        else:
            return "ongoing"
