from creatures import *
from items import *


class MapSquare:
    def __init__(self, name, description, up, down, left, right, creatures, items, links):
        self.name = name
        self.description = description
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.creatures = creatures
        self.items = items
        self.links = links

    def __repr__(self):
        return "{}".format(
            self.name
        )


world = {}
world['Castle Grounds'] = MapSquare(
    "Castle Grounds",
    "You arrive at the castle grounds and hear the unmistakable call of Baby Red, you rush towards the castle walls\n"
    "but before you can react a shape materialises in front of you. The figure laughs softly and draws a wand\n"
    "You must act now!",
    "To the north you see the castle walls stretch for hundreds of meters, there is no way through",
    "Looking to the south you see over the edge of the cliff which towers above the ravine",
    "Ahead you see the castle walls, the impenetrable barrier broken only by one large gate leading into the Forecourt",
    "You turn around and look at the Dark Forest behind you",
    creatures_castle_grounds,
    items_castle_grounds,
    {'E': 'Black Forest',
     'W': 'Castle Forecourt'}
)

world['Castle Forecourt'] = MapSquare(
    "Castle Forecourt",
    "You step over the carcass of the fallen dragon and walk cross the threshold into the castle walls.\n"
    "Upon reaching the inside of the castle you are met with a foul stench unlike anything you have experienced\n"
    "You look around and see only one door to your north, above which a tower stretches into the clouds\n"
    "A dark figure stands at a balcony hundreds of meters above you. The figure bellows something and sparks fly\n"
    "from their outstretched arm and strike the floor in front of you. From the ashes a huge, skeletal hand reaches up",
    "You look at the door below the tower, it is open",
    "To the south you can see the rest of the Forecourt, there are bones, weapons and pieces of armour scattered around",
    "To the west you can see the 30 foot walls surrounding you, there is no way out here",
    "To the east you see the way back to the Castle Grounds and the forest beyond",
    creatures_castle_forecourt,
    items_castle_forecourt,
    {'N': 'Castle Tower',
     'E': 'Castle Grounds'}
)

world['Castle Tower'] = MapSquare(
    "Castle Tower",
    "You rush through the open door and take the tower steps 3 at a time, you know the dark figure is above you somewhere...\n"
    "After a few minutes of climbing you head a low rumble and pause, the wall of the tower a few meters in front of you explodes\n"
    "and rubble tumbles past your feet, you enter the hole and see a hooded figure stand with raised wand",
    "You look up the stairs and hear gentle sobbing",
    "You look back down the staircase you just came from",
    "There is no way out",
    "There is no way out",
    creatures_castle_tower,
    items_castle_tower,
    {'N': "Red's Room",
     'S': 'Castle Forecourt'}
)

world["Red's Room"] = MapSquare(
    "Red's Room",
    "You pull yourself up the remaining stairs, the sobbing getting louder with every step you take.\n"
    "Finally you reach the top of the staircase and find Red shackled to the wall, you swing at the shackles and they break\n"
    "into hundreds of pieces. Red stops sobbing and looks at you, puzzled. You pick up Red and head off back to the mountain\n"
    "that seems to give the god their power. Upon arriving you find that you are no longer carrying Red, you can't recall\n"
    "ever putting the creature down. You look to the sky and see a blazing sunset, the fire-red clouds around it making\n"
    "the unmistakable shape of a fox.\n\n",
    "There is no way out",
    "There is no way out",
    "There is no way out",
    "There is no way out",
    creature_red_room,
    items_red_room,
    {'S': 'Castle Tower'}

)

world['Ravine'] = MapSquare(
    "Ravine",
    "You are at the bottom of a deep ravine, the water here flows with incredible power",
    "To the north you see the cliff face, there seems to be a structure at the top but you can't make it out from here",
    "To the south you see some capillaries of the river flow out into the Swampland",
    "To the west you can see the edge of a waterfall, the water torments as it gets closer to the edge of the drop",
    "To the east further down the river you can see the water become calmer and in the distance you make out your Home",
    creatures_ravine,
    items_ravine,
    {'E': 'Home',
     'S': 'Swampland'}
)

world['Swampland'] = MapSquare(
    "Swampland",
    "You sludge through the swampy marsh, there are a few shanty buildings here but it doesn't look like they\n"
    "have been used in many years",
    "To the north you can hear the river running through the Ravine, the sound is almost deafening even from here",
    "To the south the Swamp gets deeper to get through, you see the skeletons of many wild animals who have tried to go this way before",
    "To the west you can see the cliff edge Ravine runs off, its at least three hundred meters down and very steep",
    "To the east you can see the Wild Plains, you recall hunting with your father her many years ago",
    creatures_swamp,
    items_swamp,
    {'N': 'Ravine',
     'E': 'Wild Plains'}
)

world['Black Forest'] = MapSquare(
    "Black forest",
    "It's still very dark here from the thick canopy, you look around and can\n"
    "just make out a candle in a window up high to the west",
    "To the north you see a huge cliff face, it cannot be scaled",
    "To the south you peer over the edge of the cliff and see your home, the height is dizzying",
    "To the west you can see a source of light twinkling through the trees",
    "To the east you see the peak of the Mountain, the wind blowing down chills you to the bone",
    creatures_forest,
    items_forest,
    {'W': 'Castle Grounds',
     'E': 'Mountain Peak'}
)

world['Home'] = MapSquare(
    "Home",
    "You are at your home, the field spans a long way in every direction."
    "There is the smell of burning firewood coming from inside your fireplace.",
    "To the north you see cliff face, above which lies the Dark Forest. There is no way to scale the cliff",
    "To the south you see miles of Wild Plains stretching to the horizon",
    "To the west you can see the River stretch away and widen into a huge white-water torrent",
    "To the east you can see the Farmland belonging to the local village",
    creatures_home,
    items_home,
    {'E': 'Farmland',
     'S': 'Wild Plains',
     'W': 'Ravine'}
)

world['Wild Plains'] = MapSquare(
    "Wild Plains",
    "You enter the wild plains, the grass beneath your feet is heavily trampled and there are lots of animal droppings",
    "To the north you see your Home",
    "To the south you see the seemingly endless expanse of the plains, time is of the essence and there is no time to explore",
    "To the west you can see the plains get moist and slowly turn into Swampland",
    "To the east you can see the Village far away",
    creatures_wild_plains,
    items_wild_plains,
    {'E': 'Village',
     'W': 'Swampland',
     'N': 'Home'}
)

world['Foot of Mountain'] = MapSquare(
    'Foot of Mountain',
    """You leave the farmland and walk towards the mountain, which towers above you. You come across a sign which reads
    \n
    -----------------------------------
                   WARNING
    -----------------------------------
    
    This mountain is inhabited by very
           dangerous creatures!
         
       Do not proceed unless you are
     skilled in combat and prepared to
         fight for your life!
         
    -----------------------------------
                   WARNING
    -----------------------------------
    \n         
    """,
    'To the north you see the Mountain continue ahead of you',
    'To the south you see the Farmland in the distance',
    'To the west the mountain is far too steep to climb, there is only one safe path up',
    'To the east the mountain crumbles away, you can see the paths large chunks of rock have carved through the trees on their way down',
    creatures_mountain_foot,
    items_mountain_foot,
    {'N': 'Mountain Peak',
     'S': 'Farmland'}
)

world['Mountain Peak'] = MapSquare(
    "Mountain Peak",
    "You climb to the very top of the mountain and find yourself in Baby Red's cave, there are so many things you can't comprehend.\n"
    "The trinkets of a god are not to be meddled with. You find scratch marks on the floor and a large, charred hole in one of the stone walls",
    "To the north there is a the back of Baby Red's cave",
    "To the south you see the path you took up, and beyond that the Farmland many hundreds of meters down, the path is traversable",
    "To the west you can see the dark forest, the sounds coming from it are made by no animal you have ever encountered",
    "To the east you can see the sea crashing below you, there are jagged rocks lining the coast",
    creatures_mountain_peak,
    items_mountain_peak,
    {'W': 'Black Forest',
     'S': 'Foot of Mountain'}
)

world['Farmland'] = MapSquare(
    "Farmland",
    "You see a range of farm animals and crops, you stop to pet a cow on your way through and notice the carcass of a"
    "pig who wandered out of the pen. The wounds in its side are horrifying, not from any animal I know of.",
    "To the north you see the Mountain, which is both incredibly steep and filled with much more dangerous creatures",
    "To the south you see the Village, buildings of stone and wood billow sweet smelling smoke from chimneys",
    "To the west you can see your home in the distance",
    "To the east you can see the sea, waves crash against the rock-face, the sea is a little too rough to consider a swim",
    creatures_farm,
    items_farm,
    {'N': 'Foot of Mountain',
     'S': 'Village',
     'W': 'Home'}
)

world['Village'] = MapSquare(
    "Village",
    "You  enter the normally bustling village to find all the shops shut and not a single person on the streets."
    "A sign reads 'Closed until further notice after the tragic and mysterious death of Fredbas Madra 2 nights ago'",
    "To the north you see the village Farmland.",
    "To the south you see the village wall, and beyond that the Wild Plains stretch for miles.",
    "To the west you can see the edge of the Wild Plains just past the village limits, it seems deserted.",
    "To the east you can see the violent sea crashing in the distance.",
    creatures_village,
    items_village,
    {'N': 'Farmland',
     'W': 'Wild Plains'}
)
