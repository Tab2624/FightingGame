import random


class Character:
    all_characters = []
    def __init__(self, name, power = 8, health =30, armor = 8, speed = 8):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.speed = speed
        Character.all_characters.append(self)

    #Show info
    def stats(self):
        character_attributes = self.__dict__
        for key in character_attributes:
            print(f"{key}: {character_attributes[key]}")
        return self

    #method for gaining/losing health
    def lose_armor(self,amount):
        self.armor-= amount
        return self


    def gain_health(self, amount):
        self.health+= amount
        return self
    

    def lose_health(self,amount):
        self.health-= amount
        print(f"{self.name} is losing {amount} health")
        return self
    

    #method for attacking
    def attack(self, target):
        damage_amount = random.randint(0, self.power)
        #crit fail
        if damage_amount == 0:
            self.lose_health(self.power / 2)
        #do the damage
        if not target.defense(self, damage_amount):
            target.lose_health(damage_amount)
        return self



    #method for blocking
    def defense(self, attacker, damage_amount):
        speed_roll = random.randint(1, 20)
        if speed_roll <= self.speed:
            print(f"{self.name} successfully parried attack")
            self.attack(attacker)
            return True
        

    #armor
        elif damage_amount <= self.armor:
            self.lose_armor(damage_amount)
            return True
        
        print(f"{self.name} fails to defend")
        return False

class Orc(Character):
    def __init__(self, name, power=14, health=150, armor=8, speed=3):
        super().__init__(name, power, health, armor, speed)
class Shadow_Orc(Orc):
    def __init__(self, name, power=14, health=150, armor=8, speed=8):
        super().__init__(name, power, health, armor, speed)
    def attack(self, target):
        damage_amount = random.randint(0, self.power)
        #crit fail
        if damage_amount == 0:
            self.lose_health(self.power / 2)
        
        shadow_damage = random.randint(self.power /2, self.power + self.power / 2)
        #do the damage
        if not target.defense(self, damage_amount):
            print(f"{target.name} has taken SHADOW DAMAGE!")
            target.lose_health(damage_amount + shadow_damage)
        return self



class Halfling(Character):
    def __init__(self, name, power=10, health=100, armor=11, speed=17):
        super().__init__(name, power, health, armor, speed)


c1 = Character("Bob")
c2 = Character("Tom")

orc1 = Orc("Orcington")
orc2 = Shadow_Orc("Orcington's shadow brother")
halfling1 = Halfling("Bilbo")

turn_num = random.randint(0,100) % 2
players = [orc2, halfling1]

player1 = players[0]
player2 = players[1]
while player1.health > 0 and player2.health > 0:
    print("*"*80)
    if turn_num % 2 == 0:
        player1.attack(player2)
        player2.stats()
    else:
        player2.attack(player1)
        player1.stats()

    turn_num += 1