from player import *


def main():
    print_header()
    player_creation()
    game_loop()


def print_header():
    print("""
    -------------------------------------
         Snowflakes and fox tails
    -------------------------------------\n""")



def player_creation():
    global hero
    print("""
You awake to a knock at your door, it seems like forever since someone sought out your services. You rise from your
bed and stretch before ambling towards the door of your cabin. What greets you when you open the door is far from
what you expected. A short man dressed entirely in a black cloak is beaming up at you, a collection of feathers
sticking out from under his hat, perhaps to make up for the lack of hair. You open your mouth to speak but before you
get a single word out the man steps into your cabin, sits himself on the only chair and speaks""")
    time.sleep(0.5)
    hero_name = input("\n\n 'Hello there child! What do they call you then?' > ")
    time.sleep(0.5)
    print("\n----------------")
    print("""
'Well, {} I understand that you have seen your fair share of sword fights and dangerous creatures but the situation here
is far more grave than you know. This is not often information shared with common folk such as yourself, but the 
northern part of our home is filled with evil creatures that would love nothing more than to attack our beautiful village.
Now, the only thing holding them back is a Fox-God called Red who resides in the mountains...

That was until Red went missing a few days ago!!!

Without Red these beasties will make their way down into the village and lay waste to the whole region.
I need your help to bring back Red, well when I say 'your help' I really mean that you will be doing this yourself, mostly.
I will assist where I can but lets just say my strengths lay outside the realms of battle.
I recommend that you don't rush this, the animals on the north side of the region are very powerful, you will
need to get yourself some good equipment and strengthen up before you head north of the Farmland.  
Anyway I should be off, time is of the essence after all and Red is completely powerless outside of the mountain.
Oh, you should probably know my name, I am Atlantes. Good luck!'\n

Before you can even question Atlantes he is out of the door, you run out after him but see no-one in any direction...\n\n""".format(
            hero_name, hero_name
        ))
    hero = Player(hero_name, 30, 200, 10, 10, 30, 'Home')
    print('Current location:- ' + hero.position.name + '\n')
    print(hero.position.description)
    return hero


def game_loop():
    while True:
        cmd = input("\n====================================================\n"
                    "What would you like to do? Type 'Legend' for options > ")
        cmd = cmd.lower()
        if cmd == "legend":
            print("""
            Welcome! These are the inputs you can use, you can also use shortened versions of these commands,
            such as 'ln' or 'l n' for 'look north', 'd' for 'describe', 'i' for inspect:\n
            Describe - Game will describe the area you are in\n
            Look *direction* - Game will describe what is to the north, south, east, west, depending on the input\n
            Look around - Game will tell you about what is in the north, east, south AND west of you\n
            Inspect - Search your current location for anything of use, you may need to search multiple times to find everything\n
            Go *direction* - Move {} to the north, south, east or west\n
            Look for creature - Looks for a creature for you to fight\n
            Run away - Attempt to run from the animal encounter, depends on character speed and chance\n
            Attack - Attack animal, depends on many factors and chance\n
            Check status - Check the current status of {}\n""".format(hero.name, hero.name))



        # check level
        elif cmd in("look north","l n", "ln"):
            print("\n" + hero.position.up + "\n")
        elif cmd in("look south", "l s", "ls"):
            print("\n" + hero.position.down + "\n")
        elif cmd in("look east", "l e", "le"):
            print("\n" + hero.position.right + "\n")
        elif cmd in ("look west", "l w", "lw"):
            print("\n" + hero.position.left + "\n")
        elif cmd in ("describe", "d", "d"):
            print("\n" + hero.position.description + "\n")
        elif cmd in ("look around", "la", "l a"):
            print(
                "\n" + hero.position.up + "\n" + hero.position.down + "\n" + hero.position.left + "\n" + hero.position.right + "\n")
        elif cmd == "check status":
            print("""
            Your name is {}
            Your current level is {}
            Your current health is {}
            Your current armour level is {}
            Your current attack level is {}
            Your current speed is {}
            You are currently in the area known as {}\n"""
                  .format(hero.name, hero.level, round(hero.health), hero.armour, hero.attack, hero.speed, hero.position))
        elif cmd in ('inspect area', 'inspect', 'i'):
            hero.inspect()
        elif cmd in('look for creature', 'lfc', 'l f c', 'lc', 'l c'):
            hero.creature_spawn()
        elif cmd in ('go north', 'g n', 'gn'):
            hero.move('N')
        elif cmd in ('go south', 'g s', 'gs'):
            hero.move('S')
        elif cmd in ('go east', 'g e', 'ge'):
            hero.move('E')
        elif cmd in ('go west', 'g w', 'gw'):
            hero.move('W')
        else:
            print("Sorry, I don't understand that input\n")


# rewrite move command in player

if __name__ == '__main__':
    main()
