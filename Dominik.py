from Game import *

def starting_point():
    choice_1 = input("""You look around to orientate yourself, you seem to be standing in a courtyard, to your right is a graveyard.
To your left you see an abandoned well, it is mossy and seems so old it is ready to fall apart.
Behind you is a giant entrance gate, the whole area is surrounded by a dark, eerie, forest and a thick fog obscuring your vision.
In front of you is a giant mansion, it looks very old, it is covered in moss, some of the windows are broken.""")
    if "left" or "well" in choice_1: 
        well()
    if "right" or "graveyard" in choice_1:
        graveyard()
    if "behind" or "gate" in choice_1:
        gate()
    if "mansion" in choice_1:
        door()
    if "window" in choice_1:
        window()

def gate():
    print("""You go up to the gate, it is rusty but still stands sturdy. 
The path beyond leads into an engulfing darkness. 
You leave after realising there is not escape.""")
    starting_point()

def graveyard():
    choice_graveyard = input("""You enter the graveyard. 
The forg here is more dense than in the other areas. 
You see a tree a shed and a few graves.
Where will you go?""")
    if "tree" in choice_graveyard:
        tree()
    if "shed" in choice_graveyard:
        shed()
    if "grave" or "graves" in choice_graveyard:
        graves()

def graves():
    choice_graves = int(input("""There are four graves which do you want to examine?"""))
    if int(1) in choice_graves:
        print()
    if int(2) in choice_graves:
        print()
    if int(3) in choice_graves:
        print()
    if int(4) in choice_graves:
        print()

def shed():
    choice_shed = input("""You go up to the shed and push the door, it creaks open.
Do you go in?""")
    if "yes" or "enter" in choice_shed:
        inside_shed()
    if "no" or "leave" in choice_shed:
        graveyard()

#you figt something here before you leave the shed. also shovel is added as an item in inventory 
def inside_shed():
    print("""Inside the shed is firewood and some other useless things. 
You find a shovel and take it with you.""")

#if i dig without shovel in inventory it wont dig, but if i have it will... and if i dig it up i get reward in inv. i cba typing now so isak and theo help me lul
def tree():
    choice_tree = input("""You go up to the tree. 
The tree itself is not suspicious, although there is a recenty dug up path next to it.
Do you want dig?""")
    if "dig" or "yes" in choice_tree:
        print()
    if "no" or "leave" in choice_tree:
        print()

def dug_up():
    print("""You find an axe, it is probably the one the firewood had been cut with.
It seems in good condition, it was buried not too long ago.
You leave the tree and return to the graveyard.""")
    graveyard()

#need to finish this shite
def digging_failed():
    print("""You dig but it is not going too well, the ground is too hard. 
You need something to dig with...""")

def well():
    choice_well = input("""The well looks ready to fall apart, the rope seems well attacked and should hold your weight. 
Do you want to go down the rope?""")
    if "yes" or "down" in choice_well:
        well_bottom()
    if "no" or "leave" in choice_well:
        starting_point()

#get attacked kekw, when win you go to the dungeon()
def well_bottom():
    print("""The bottom of the well is dry, there is a hole in the wall. 
You see a green light at the end of the tunnel. 
The green light is coming from some weird flowers you have never seen before, it would be safest not to touch them. 
The hole leads into a large cave, it seems to be located underneath the mansion.""")

#need key to open
def dungeon():
    print("""The hole leads to a cell in a dungeon.
The door is locked, you can not open it from the inside, but if you had a key you could open the door...""")

def mansion_inside():
    choice_mansion = input("""You come into the mansion through a door in the basement, you go up to the mansion's groud floor.
It is quiet inside the mansion, there is dust everywhere.
You hear some noises from the attic.
Do you go up to the attic?""")
    if "yes" or "attic" in choice_mansion:
        attic()
    if "no" or "leave" in choice_mansion:
        print("""Dr.G: You've come this far, this far, there is no turing back now...
    You look back to where the door had been and see it is gone, you go up to the attic.""")
        attic()

###the mirror ask you a semi hard riddle, you can either solve it or fight the mirror, 
#your reflection comes out of the mirror and attacks you, it will be a challenge. or you can just be smart and stride towards and destroy it lol losers. 
def attic():
    print(f"""Inside the attic you find a lone mirror, you go up to it.
Your reflection copies your movements perfectly... untill it doesn't.
Mirror: 

Mirror: So you have chosen death. It shall be as you wish it. 
You come out of the mirror bearing {weapon}, 



I make two people out of one. What am I?
Mirror 
Yes! That is correct, it is I! A "\mirror/".

Always in you, Sometimes on you; If I surround you, I can kill you. What am I?
Water
Mirror: Yes it is "\water/"!

Mirror: You use a knife to slice my head and weep beside me when I am dead. What am I?
Onion
Mirror: Yes that is correct, the answer is "\onion/".


Mirror: No, you have 2 more chances to get the right answer, or else.
Mirror: Last chance to get the write answer... Think long and hard about this.



Mirror: You have been very entertaining, you may pass. 
And earn your freedom.

Wrong! HAHAHAHA, you failed. 
Now you will be punished.


""")

#Get attacked by something if loose go back to start no text either, if win leave and read text 
def window_room():
    print("""The room yoou entered is full of dust. No one has been here in a while.
You go up to a desk and examine some documents.""")

#if you knock too much you get killed lmao, 
def door():
    choice_door = input("""The mansion door is giant, you try to open the door but it is closed and will not budge.
Will you try to knock the door?""")
    if "yes" or "knock" in choice_door:
        print()
    if "no" or "leave" in choice_door:
        starting_point()

def window():
    choice_window = input("""You look through the window and see a dark room, the room seems empty. 
Dr.G if you go into the room you are sure to have fun, hehe...
Do you enter or do you leave?""")
    if "leave" or "back" in choice_window:
        starting_point()
    if "enter" or "go in" in choice_window:
        window_room()

def start():
    print("""Dr.G: Welcome to SCP-6969420-2 D-Class-69420. You have done well completing the 1st stage.
I am very happy with your progress. You have already beaten 40% of our other D-Classes. 
I hope you continue to suprise us with your intellect. Complete this challenge to get to the next level, and reach your reward, of freedom.""")
    starting_point()

start()