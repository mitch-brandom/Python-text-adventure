
class Weapons:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    def equip(self, hero):
        ans = 0
        while ans not in ('yes', 'y', 'no', 'n'):
            ans = input("You search the area and see a {}. Would you like to equip it? Its attack is {}, your current attack is {} "
                    .format(self.name, self.attack, hero.attack))
            ans = ans.lower()
            if ans in ('yes', 'y'):
                hero.attack = self.attack
                print('\nYou inspect your new {}, it boosts your attack points to {}! '.format(self.name, hero.attack))
                hero.position.items.remove(self)
            elif ans in ('no', 'n'):
                return
            elif ans not in ('yes', 'y', 'no', 'n'):
                print("Sorry, I didn't understand that")



class Clue:
    def __init__(self, name, clue):
        self.name = name
        self.clue = clue

    def equip(self, hero):
        ans = 0
        while ans not in ('yes', 'y', 'no', 'n'):
            ans = input("\nYou check your surroundings and see a {}. Would you like to look closer?  "
                        .format(self.name))
            ans = ans.lower()
            if ans in ('yes', 'y'):
                print(self.clue)
                hero.position.items.remove(self)
            elif ans in ('no', 'n'):
                return
            elif ans not in ('yes', 'y', 'no', 'n'):
                print("Sorry, I didn't understand that")



class Armour:
    def __init__(self, name, armour):
        self.name = name
        self.armour = armour

    def equip(self, hero):
        ans = 0
        while ans not in ('yes', 'y', 'no', 'n'):
            ans = input("\nYou look around and find a {}. Would you like to equip it? Its armour rating is {}, your current armour is {}  "
                    .format(self.name, self.armour, hero.armour))
            ans = ans.lower()
            if ans in ('yes', 'y'):
                hero.armour = self.armour
                print('\nYou inspect your new {}, it boosts your armour points to {}!'.format(self.name, hero.armour))
                hero.position.items.remove(self)
            elif ans in ('no', 'n'):
                return
            elif ans not in ('yes', 'y', 'no', 'n'):
                print("Sorry, I didn't understand that")


class Health:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def equip(self, hero):
        ans = 0
        while ans not in ('yes', 'y', 'no', 'n'):
            ans = input("\nYou search around you and find a {}. Would you like to use it? It will heal {} points, your current health is {}  "
                    .format(self.name, self.health, hero.health))
            ans = ans.lower()
            if ans in ('yes', 'y'):
                hero.health = hero.health + self.health
                if hero.health > 200:
                    hero.health = 200
                print('\nYou use the {}, it heals you instantly! Your new health is {}!'.format(self.name, hero.health))
                hero.position.items.remove(self)
            elif ans in ('no', 'n'):
                return
            elif ans not in ('yes', 'y', 'no', 'n'):
                print("Sorry, I didn't understand that")



items_castle_grounds = [
    Armour('Dragon Scale Chainmail', 140),
    Clue('Scratches on gateway', '\nYou see scratches around the gateway to the forecourt\n'),
    Health('Vial of Dragons Blood', 100),
    Health('Medium Health Potion', 50)

]

items_castle_forecourt = [
    Weapons("Minotaur's Broadsword", 150),
    Health('Large Health Potion', 75),
    Health('Large Health Potion', 75)

]

items_castle_tower = [

]

items_red_room = [

]

items_ravine = [
    Armour('Rusty Chainmail', 25),
    Weapons('Damaged mace', 27),
    Health('Raw fish', 12),
    Health('Waterlilly', 5),
    Health('Raw fish', 15)

]

items_swamp = [
    Health('Medium Health Potion', 50),
    Weapons('Bronze Spear', 33),
    Armour('Crocodile skin clothing', 35)

]

items_forest = [
    Weapons('Mystic Sword', 100),
    Armour ('Enchanted suit of armour', 110),
    Health('Large Health Potion', 75),
    Health('Medium Health Potion', 50),
    Health('Medium Health Potion', 50),
    Clue("Red's fur", "\nYou see a clump of Red's fur lying on the ground, you must be heading the right way\n"),
    Clue("Scorch marks", "\nYou see scorch marks at the tops of the trees, what could do that?\n")



]

items_home = [
    Weapons('Rusty Sword', 12),
    Armour('Hunters clothes', 15),
    Clue ("Atlantes' note", "\nGood luck Adventurer! Don't go near the mountain until you are ready!\n"
                            "Make sure you inspect your surroundings for items you can use on your quest\n")

]

items_wild_plains = [
    Weapons('Steel Shortsword', 25),
    Health('Cooked Meat', 15),
    Health('Small Health Potion', 30),
    Armour('Battered Chainmail', 28),
    Clue('Symbols scratched into dirt', """\n
         ^       ^                	 _____
        /|\     /|\                 /     \ 
        /|\     /|\                | () () |
        /|\     /|\        =        \  ^  /
         |       |                   |||||
                                     |||||
    \n
    """)

]

items_mountain_foot = [
    Clue('Severed head', '\nThe head appears to be from someone around your age, you look up the mountain and can make out\n'
                         'splashes of blood it must have left as it tumbled down\n'),
    Health('Cooked Meat', 15),
    Health('Small Health Potion', 30),
    Health('Medium Health Potion', 50),
    Weapons('Steel Longsword', 40),
    Armour('Full chainmail', 45)

    
    
    
]

items_mountain_peak = [
    Clue('Scratches on the floor', "\nYou notice that among the scratches there is a perfectly formed arrow pointing"
                                   "towards the Dark Forest behind you\n"),
    Weapons('Mithril Sword', 75),
    Armour('Full Chainmail with Breastplate', 70),
    Health('Cooked meat', 25),
    Health('Medium Health Potion', 50),
    Health('Large Health Potion', 75)
    
    

]

items_farm = [
    Weapons('Pitchfork', 18),
    Armour('Cow Hide Suit', 20),
    Health('Pint of milk', 15),
    Health('Raw eggs', 20),
    Clue('Scrunched up note', "\nThe note reads: 'I heard some scuffling and an otherworldly roar from the mountain"
                              " north of here a few nights ago. \n"
                              "I would investigate but the creatures there are too powerful'\n")

]

items_village = [
    Weapons('Iron Sword', 25),
    Armour('Iron Chestplate', 30),
    Clue('Scruffy drawing', """\n
    
      --------------------N---------------------
    NW|  Castle  |  Black Forest  |  Mountain  |NE
      |---------- ----------------
     W|  Ravine  |   Lone house   |  Farmland  |E
      |
    SW|  Swamp   |   Wild Plains  | Village    |SE
      --------------------S---------------------
    
            \n""")
]
