from map import *
import random
import secrets
import sys


class Player:
    def __init__(self, name, level, health, armour, attack, speed, position):
        self.name = name
        self.level = level
        self.health = health
        self.armour = armour
        self.attack = attack
        self.speed = speed
        self.position = world[position]

    def move(self, direction):
        global active_creature
        if direction not in self.position.links:
            print("You cannot go this way! Look around to see what the terrain is like")
            return
        new_position = self.position.links[direction]
        self.position = world[new_position]
        print('You have arrived at the ' + self.position.name + '\n')
        print(self.position.description + '\n\n')
        if self.position == world["Red's Room"]:
            print("You win!")
            sys.exit()

        active_creature = 0
        rnd = random.randrange(1, 100)
        if rnd in range(1, 100):
            self.creature_spawn()
        else:
            return

    def inspect(self):
        x = random.randint(1, 100)
        if len(self.position.items) == 0:
            print('\nThere is nothing else to find here')
        else:
            item1 = random.choice(self.position.items)
            item2 = secrets.choice(self.position.items)
            item3 = random.choice(self.position.items)
            items = (item1, item2, item3)
            active_item1 = random.choice(items)
            active_item1.equip(self)


        #else:
            #print('You found nothing')
            #return

    def creature_spawn(self):
        active_creature = 0
        creature1 = random.choice(self.position.creatures)
        creature3 = secrets.choice(self.position.creatures)
        creatures = (creature1, creature3)
        active_creature = random.choice(creatures)
        if active_creature == None:
            print("There doesn't appear to be any creatures in the area")
            return
        else:
            action = input(
                'You encounter a {} of level {}!!\nYou can attack or try to run home. What would you like to do? > '.format(
                    active_creature, active_creature.level))
        action = action.lower()
        while True:
            if action == 'run' or action == 'r':
                self.run(active_creature)
                return False
            elif action == 'attack' or action == 'a':
                self.fight(active_creature)
                return False
            else:
                action = input("Sorry, I didn't understand that ")

    def run(self, active_creature):
        while True:
            print("You try to run from the {}".format(active_creature))
            my_roll = self.speed_roll()
            creature_roll = active_creature.speed_roll()
            if my_roll >= creature_roll:
                print('You managed to escape from the {}'.format(active_creature))
                self.position = world['Home']
                self.health = 200
                print (self.position.description)
                return False
            else:
                print('The {} is too quick for you, there is no choice now but to fight! '.format(active_creature))
                time.sleep(0.5)
                active_creature.fight(self)
                return False

    def fight(self, active_creature):
        while True:
            print('\nYour current health is {}\n'.format(round(self.health)))
            print("The {}'s current health is {}\n".format(active_creature.name, round(active_creature.health)))
            time.sleep(0.5)
            my_roll = self.attack_roll() * 1.2
            creature_roll = active_creature.defence_roll()
            health_roll = (my_roll - creature_roll) + (self.level / 3) - (active_creature.level / 2)

            if my_roll <= creature_roll:
                print('You lunge at the {} but it dodges at the last moment! Brace yourself for its counter.\n'
                      .format(active_creature.name))
                time.sleep(0.5)
                active_creature.fight(self)
                return False
            else:
                if health_roll < 30:
                    health_roll = random.randint(30, 40)
                print('You land a heavy blow on the {}! You deal {} damage\n'.format(active_creature.name, round(health_roll)))
                active_creature.health = active_creature.health - round(health_roll)
                if active_creature.health > 0:
                    # print("The {}'s health is now {}. Be prepared for its next attack".format(active_creature.name, round(active_creature.health)))
                    time.sleep(0.5)
                    active_creature.fight(self)
                    return active_creature.health
                else:
                    print("You've defeated the {}! Well done!\n".format(active_creature))
                    self.level = (self.level + round(active_creature.level / 5))
                    if self.level >= 250:
                        self.level = 250
                    print("Your new level is {}\n".format(round(self.level)))
                    active_creature.health = 100
                    active_creature = 0
                    return False, active_creature

    def speed_roll(self):
        return random.randint(1, 50) + self.speed + round(self.level)

    def defence_roll(self):
        return random.randint(1, 50) + self.armour + round(self.level)

    def attack_roll(self):
        return random.randint(1, 50) + self.attack + round(self.level)
