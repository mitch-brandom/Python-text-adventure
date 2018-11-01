import random
import time


class Creature:
    def __init__(self, name, level, health, armour, attack, speed):
        self.name = name
        self.level = level
        self.health = health
        self.armour = armour
        self.attack = attack
        self.speed = speed

    def __repr__(self):
        return "{}".format(
            self.name
        )

    def speed_roll(self):
        return random.randint(1, 50) + self.speed + round(self.level)

    def defence_roll(self):
        return random.randint(1, 50) + self.armour + round(self.level)

    def attack_roll(self):
        return random.randint(1, 50) + self.attack + round(self.level)

    def fight(self, hero):
        from player import Player
        from map import world
        while True:
            print("The {} prepares to attack you".format(self.name))
            my_roll = hero.defence_roll() + hero.level
            creature_roll = self.attack_roll() + self.level
            health_roll = abs(my_roll - creature_roll) + (self.level / 3)
            if my_roll >= creature_roll:
                print('The {} flies at you with all of its strength, but you block the attack!'.format(self.name))
                time.sleep(0.5)
                Player.fight(hero, self)
                return False
            else:
                print('The {} lands its attack! You lose {} health'.format(self.name, round(health_roll)))
                hero.health = hero.health - round(health_roll)
                time.sleep(0.2)
                if hero.health <= 0:
                    print('You were defeated by the {}, you start to black out!'.format(self.name))
                    time.sleep(2)
                    print("""
You awake to the sound of a door closing, you open your eyes and realise you are in your home, 
but when you look around your house is empty, except for a single feather resting on the chair\n""")
                    hero.health = 200
                    hero.position = world['Home']
                    return False
                else:
                    time.sleep(0.5)
                    Player.fight(hero, self)
                    return hero.health



# attack
# defence
# run

creatures_castle_grounds = [

    Creature('Dragon', random.randint(100, 150), 250, 180, 175, 100)
]

creatures_castle_forecourt = [
    Creature('Undead Minotaur', random.randint(150, 200), 300, 180, 175, 100)
]

creatures_castle_tower = [
    Creature('Dark Wizard', random.randint(200, 250), 350, 200, 200, 100)
]

creature_red_room = [
    None
]

creatures_ravine = [
    Creature('Crocodile', random.randint(20, 30), 100, 35, 20, 30),
    Creature('Huge Poisonous Toad', random.randint(10, 18), 100, 20, 15, 5),
    Creature('Mermaid', random.randint(25, 35), 100, 30, 20, 50)
]

creatures_swamp = [
    Creature('Crocodile', random.randint(25, 35), 100, 50, 35, 15),
    Creature('Huge Lizard', random.randint(30, 35), 100, 40, 20, 20),
    Creature('Dark Fairy', random.randint(30, 40), 100, 40, 25, 60)
]

creatures_forest = [
    Creature('Chimera', random.randint(85, 110), 250, 100, 125, 40),
    Creature('Werewolf', random.randint(90, 120), 225, 95, 150, 60),
    Creature('Skeletal Horseman', random.randint(90, 110), 200, 100, 125, 50)
]

creatures_home = [None

]

creatures_wild_plains = [
    Creature('Bison', random.randint(10, 30), 100, 25, 10, 7),
    Creature('Lion', random.randint(30, 45), 100, 40, 40, 40),
    Creature('Eagle', random.randint(20, 35), 100, 30, 40, 80)

]

creatures_mountain_peak = [
    Creature('Griffin', random.randint(75, 90), 180, 75, 80, 80),
    Creature('Wendigo', random.randint(80, 110), 175, 60, 90, 30),
    Creature('Gargoyle', random.randint(80, 120), 150, 65, 95, 20),

]

creatures_mountain_foot = [
    Creature('Mountain Lion', random.randint(50, 70), 130, 50, 75, 25),
    Creature('Elder Wolf', random.randint(45, 65), 125, 60, 60, 40),
    Creature('Troll', random.randint(60, 75), 150, 70, 50, 20),


    ]

creatures_farm = [
    Creature('Wolf', random.randint(20, 40), 100, 30, 20, 30),
    Creature('Hawk', random.randint(10, 25), 100, 30, 20, 30),
    Creature('Bison', random.randint(15, 30), 100, 30, 25, 7),

]

creatures_village = [None

               ]
