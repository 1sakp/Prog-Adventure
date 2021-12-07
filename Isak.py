from Game import *
def start_isak():
    choise = input("""You enter contiusness and look at your suroundings.
          You see a path to the right and the left.
          Dr.G: Now go left and win the Trial of Champions, it won't be too hard.
          Where do you want to go:  """)
    if "left" in choise.lower():
        print("""You enter what looks like an arena like that from ancient greece.
              Dr.G: You should see a arena now, do you see it?""")
    if "right" in choise.lower():
        choise = input("""Dr.G: NO! Don't go there. We don't know what will happen, you could DIE! Now turn back and continue on course.
                       Do you want to continue?:    """)
        if "yes" in choise.lower():
            print("""You find the item""")
        
        
        