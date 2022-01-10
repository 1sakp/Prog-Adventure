from Game import *
import subprocess as sub

def arena_door_right():
      global player_hp
      print(f"You take 5 points of damage as you step on some spikes. This makes you back out of the room...")
      player_hp -= 5
      arena_corridor()

def arena_door_left():
      print(f"You enter the room, to your suprise there is no furiture in this room. You decide to walk out again...")
      arena_corridor()
      
def arena_door_middle():
      choise = input(f"You enter what apears to be a room with a book case and nothing else...")
      if "take" or "grab" or "book" in choise.lower():
            exec(open("Theo.py").read())
      if "exit" or "leave" in choise.lower():
            arena_corridor()

def arena_corridor():
      choise = input("""You enter a corridor with 3 rooms, one on the left, one on the right and one in the middle:  what door do you wish to enter? :   """)
      if "right" in choise.lower():
            arena_door_right()
      if "left" in choise.lower():
            arena_door_left()
      if "middle" or "center" in choise.lower():
            arena_door_middle()

def arena():
      global player_hp
      global weapon
      choise = input(f"""You enter The Arena and see a locál looking like the Colosseum.
                     Dr.G: Ah... yes! Finally the trial. Lets see if you have what it takes...
                     Several Rats with {rat[0]}HP and they do {rat[1]}dmg.""")
      attack(rat)
      attack(rat)
      attack(rat)
      attack(archer)
      choise = input(f"""Dr.G: You can now upgrade your sword or drink a health-potion: choose wisely:      """)
      if "drink" or "potion" or "health" in choise.lower():
            player_hp += 50
            if player_hp > 100:
                  player_hp = 100
            print(f"You HP is now {player_hp}...")
      elif "sword" or "upgrade" in choise.lower():
            weapon["sword of smiting"] += 2
      attack(rat)
      print("You leave the arena and go thrugh a door.")
      arena_corridor()
      
def start_isak_2():
      choise = input("""You see a path to the right and the left.
                        Dr.G: Now go left and win the Trial of Champions, it won't be too hard.
                        Where do you want to go:  """)
      if "right" in choise.lower():
            print("""You have already been there!""")
            start_isak_2()
      if "left" in choise.lower():
            arena()
      
def start_isak():
    choise = input("""You enter contiousness and look at your suroundings.
                      Dr.G: Now go left and win the Trial of Champions, it won't be too hard.
                      You: The what?!
                      DR.G: Don't worry just follow my instructions...
                  You see a path to the right and the left.
                  The left path seems to lead to a ancient arena.
                  The right path leads to some sort of shrine.
                  Where do you want to go:  """)
    if "left" in choise.lower():
        print("""You enter what looks like an arena like that from ancient greece.
              Dr.G: You should see a arena now, do you see it?""")
        arena()
    if "right" in choise.lower():
        choise = input("""Dr.G: NO! Don't go there. We don't know what will happen, you could DIE! Now turn back and continue on course.
                       Do you want to continue?:    """)
        if "yes" in choise.lower():
            puzzle = str(input("""You find a sword laying on a table and a tablet. You read the tablet:
                  "To gain power you must be smart, solve this puzzle and gain the 'Sword of Smiting':
                  
                  || |
                  || |
                  | ||
                  
                  Dr.G: It seems this is the puzzle. Look you can input three numbers. I wonder what the answer is!
                  You can input 3 numbers without whitespaces:     """))
            puzzle = puzzle.replace(" ", "")
            if puzzle == "332":
                  inventory.append(items[0])
                  print(f"""You now have {inventory} in your inventory.""")
                  print("""De.G: Now go to The Arena, you lucky person... you really culd have died!
                        You decide to go to back to where you woke up.""")
                  start_isak_2()
                  
            else:
                  print("You lost, bad luck... You shall die now!")
                  dead("not listening to the advice he was given")

print("""You wake up on a plain hospital bed in a unfurnished room...
         You don't remember annything... you where in prisson but now... now...
         A voice interuppts your thoughts... 
         
         Unkown: D-Class... D-Class wake up we need to experiment...
         You: What do you mean... where am I?
         Unknown: Ah yes... I see the sedetive was a bit to strong, interesting... annyway I'm Dr.G and you are in the testing area for SCP-6969420.
         You: What!
         Dr.G: No time to explain. Look in to the circular object on your right!
         
         What you previusly had thought to be an unfurnished room now has somthing looking like a mirror in it.
         
         Dr.G: Hurry up we havent got all day!
         
         You nevusly look in to the mirror like object, expecting there to be something strange about it...
         but before you notice annything unusual you suddenly black out!
         
         """)

start_isak()