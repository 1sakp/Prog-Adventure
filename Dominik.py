from Game import *

def start():
    print("""Welcome to SCP-6969420-2 D-Class-69420. You have done well completing the 1st stage.
I am very happy with your progress. You have already beaten 40% of our other D-Classes. 
I hope you continue to suprise us with your intellect. Complete this challenge to get to the next level, and reach your reward, of freedom.""")

    choice_1 = input("""You look around to orientate yourself, you seem to be standing in a courtyard, to your right is a graveyard.
To your left you see an abandoned well, it is mossy and seems so old it is ready to fall apart.
Behind you is a giant entrance gate, the whole area is surrounded by a dark, eerie, forest and a thick fog obscuring your vision.
In front of you is a giant mansion, it looks very old, also covered in moss, some of the windows are broken.""")
    if "left" in choice_1: 
        print()
    if "right" in choice_1:
        print()
    if "behind" or "gate" in choice_1:
        print()
    if "mansion" or "window" in choice_1:
        print()

start()