
#variabler
last = "placeholder"

#system designat av Isak
items = ["sword of smiting", "fist"]
inventory = []
inventory.append(items[1])
player_hp = 100

#template för varelser, först i listan är HP sen DMG sen namn: system designat av Isak
rat = [10, 1, "Rat"]
skeleton = [15, 2, "Skeleton"]
troll = [30, 2, "Troll"]
archer = [5, 4, "Archer"]
mirror_being = [75, 7, "Your Reflection"]
rotting_corpse = [20, 3, "Rotting Corpse"]
spectre = [20, 3, "Spectre"]

#stringen är bara namnet på vapnet. Numret efter är skadan vapnet gör  ####Isak
weapon = {
    "fist": 1,
    "sword of smiting": 5,
    "iron sword": 3,
    "steel shovel": 3,
    "axe": 4,
}

#Theo
def dead(dead):
    print(f"Dr. G: The D class died while {dead}. ")
    exit()

#Isak:  så att man kan öppna sitt inventory och se vad man har
def inv():
    print(f"You open your bag and find:  {inventory}")


#Isaks AMAZING ATTACK system: argumentet är bara en av varelsena.   //MVH Isak
def attack(creature):
    global player_hp
    global last
    creature_name = creature[2]
    creature_hp = creature[0]
    print(f"You are fighting a {creature_name}!")
    choice = (input(f"You have {inventory} in your inventory. (Chose a weapon: use only singular or use 'last' to use last weapon used):    "))
    if "last" in choice.lower():
        weapon_local = weapon[last]
        creature_dmg = creature[1]
        while True:
            if player_hp >= 1:
                if creature_hp >= 1:
                    player_hp = player_hp - creature_dmg
                    creature_hp = creature_hp - weapon_local
                    print(f"You did {weapon[last]} dmg, the {creature_name} has {creature_hp}HP left!")
                    print(f"The {creature_name} attacks you and does {creature_dmg} you have {player_hp}HP left!")
                else:
                    print("You won!")
                    return()
            else:
                dead(f"fighting a {creature_name}")
    else:
        last = choice.lower()
        weapon_local = weapon[choice.lower()]
        creature_dmg = creature[1]
        while True:
            if player_hp >= 1:
                if creature_hp >= 1:
                    player_hp = player_hp - creature_dmg
                    creature_hp = creature_hp - weapon_local
                    print(f"You did {weapon[choice.lower()]} dmg, the {creature_name} has {creature_hp}HP left!")
                    print(f"The {creature_name} attacks you and does {creature_dmg} you have {player_hp}HP left!")
                else:
                    print("You won!")
                    return()
            else:
                dead(f"fighting a {creature_name}")  

def starting_point():
    choice_1 = input("""You look around to orientate yourself, you seem to be standing in a courtyard, to your right is a graveyard.
To your left you see an abandoned well, it is mossy and seems so old it is ready to fall apart.
Behind you is a giant entrance gate, the whole area is surrounded by a dark, eerie, forest and a thick fog obscuring your vision.
In front of you is a giant mansion, it looks very old, it is covered in moss, some of the windows are broken.""")
    if "left" in choice_1.lower() or "well" in choice_1.lower(): 
        well()
    if "right" in choice_1.lower() or "graveyard" in choice_1.lower():
        graveyard()
    if "behind" in choice_1.lower() or "gate" in choice_1.lower():
        gate()
    if "mansion" in choice_1.lower():
        door()
    if "window" in choice_1.lower():
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
    if "tree" in choice_graveyard.lower():
        tree()
    if "shed" in choice_graveyard.lower():
        shed()
    if "grave" or "graves" in choice_graveyard.lower():
        graves()

def graves():
    choice_graves = int(input("""There are four graves which do you want to examine?"""))
    if 1 in choice_graves:
        print()
    if 2 in choice_graves:
        print()
    if 3 in choice_graves:
        print()
    if 4 in choice_graves:
        print()

def shed():
    choice_shed = input("""You go up to the shed and push the door, it creaks open.
Do you go in?""")
    if "yes" or "enter" in choice_shed.lower():
        inside_shed()
    if "no" or "leave" in choice_shed.lower():
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
    if "dig" or "yes" in choice_tree.lower():
        print()
    if "no" or "leave" in choice_tree.lower():
        print()

def dug_up():
    print("""You find an axe, it is probably the one the firewood had been cut with.
It seems in good condition, it was buried not too long ago.
You leave the tree with the axe and return to the graveyard.""")
    inventory.append
    graveyard()

#need to finish this shite
def digging_failed():
    print("""You dig but it is not going too well, the ground is too hard. 
You need something to dig with...""")

def well():
    choice_well = input("""The well looks ready to fall apart, the rope seems well attacked and should hold your weight. 
Do you want to go down the rope?""")
    if "yes" or "down" in choice_well.lower():
        well_bottom()
    if "no" or "leave" in choice_well.lower():
        starting_point()

def well_bottom():
    print("""The bottom of the well is dry, there is a hole in the wall. 
You see a green light at the end of the tunnel. 
The green light is coming from some weird flowers you have never seen before, it would be safest not to touch them. 
The hole leads into a large cave, it seems to be located underneath the mansion.""")
    attack(troll)
    attack(troll)
    attack(troll)
    if player_hp <= 0:
        print(f"You have died in battle against a {spectre}")
        dead()
    elif player_hp >= 1:
        print("You win by the skin of your teeth.")
        dungeon()
    if player_hp >= 25:
        print("You are victorious with grave injuries.")
        dungeon()
    if player_hp >= 50:
        print("You win with minor inconvinences.")
        dungeon()
    if player_hp >= 75:
        print("You call this a challenge? Hah.")
        dungeon()

#need key to open
def dungeon():
    print("""The hole leads to a cell in a dungeon.
The door is locked, you can not open it from the inside, but if you had a key you could open the door...""")

def mansion_inside():
    choice_mansion = input("""You come into the mansion through a door in the basement, you go up to the mansion's groud floor.
It is quiet inside the mansion, there is dust everywhere.
You hear some noises from the attic.
Do you go up to the attic?""")
    if "yes" or "attic" in choice_mansion.lower():
        attic()
    if "no" or "leave" in choice_mansion.lower():
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
    print("You enter the mirror and find yourself back in the same dreadful hospital room before falling unconscious.")
    Theo_game_intro()

#Get attacked by something if loose go back to start no text either, if win leave and read text 
def window_room():
    print("""The room yoou entered is full of dust. No one has been here in a while.
You go up to a desk and examine some documents.
The shadows around you start moving, you take up battle stance.""")
    attack(spectre)
    attack(spectre)
    if player_hp <= 0:
        print(f"You have died in battle against a {spectre}")
        dead()
    elif player_hp >= 1:
        print("You win by the skin of your teeth.")
    if player_hp >= 25:
        print("You are victorious with grave injuries.")
    if player_hp >= 50:
        print("You win with minor inconvinences.")
    if player_hp >= 75:
        print("You call this a challenge? Hah.")

#if you knock too much you get killed lmao, 
def door():
    choice_door = input("""The mansion door is giant, you try to open the door but it is closed and will not budge.
Will you try to knock the door?""")
    if "yes" or "knock" in choice_door.lower():
        knock_count = 0
        while knock_count < 3:
            
    if "no" or "leave" in choice_door.lower():
        starting_point()

def window():
    choice_window = input("""You look through the window and see a dark room, the room seems empty. 
Do you enter or do you leave?""")
    if "leave" or "back" in choice_window.lower():
        starting_point()
    if "enter" or "go in" in choice_window.lower():
        window_room()

def start_dominik():
    print("""Dr.G: Welcome to SCP-6969420-2 D-Class-69420. You have done well completing the 1st stage.
I am very happy with your progress. You have already beaten 40% of our other D-Classes. 
I hope you continue to suprise us with your intellect. Complete this challenge to get to the next level, and reach your reward, of freedom.""")
    starting_point()







#START ISAK
#definitioner/olika platser och rum
def arena_door_right():
      global player_hp
      print(f"You take 5 points of damage as you step on some spikes. This makes you back out of the room...")
      player_hp -= 5
      arena_corridor()

def arena_door_left():
      print(f"You enter the room, to your suprise there is no furiture in this room. You decide to walk out again...")
      arena_corridor()
      
def arena_door_middle():
      choice = input(f"You enter what apears to be a room with a book case and nothing else...")
      if "take" or "grab" or "book" in choice.lower():
            print("""
You wake up in the hospital bed again""")
            start_dominik()
      elif "exit" or "leave" in choice.lower():
            arena_corridor()

def arena_corridor():
      choice = input("""
You enter a corridor with 3 rooms, one on the left, one on the right and one in the middle:  what door do you wish to enter? :   """)
      if "right" in choice.lower():
            arena_door_right()
      if "left" in choice.lower():
            arena_door_left()
      if "middle" or "center" in choice.lower():
            arena_door_middle()

def arena():
      global player_hp
      global weapon
      print(f"""
You enter The arena and see an structure looking like the Colosseum.
Dr.G: Ah... yes! Finally the trial. Lets see if you have what it takes...
Several Rats with {rat[0]}HP and they do {rat[1]}dmg.""")
      attack(rat)
      attack(rat)
      attack(rat)
      attack(archer)
      print("""
Dr.G: Now drink a health-potion      """)
      player_hp += 50
      if player_hp > 100:
            player_hp = 100
      print(f"You HP is now {player_hp}...")
      attack(rat)
      print("You leave the arena and go thrugh a door.")
      arena_corridor()
      
def start_isak_2():
      choice = input("""
You see a path to the right and the left.
Dr.G: Now go left and win the Trial of Champions, it won't be too hard.
Where do you want to go:  """)
      if "right" in choice.lower():
            print("""You have already been there!""")
            start_isak_2()
      if "left" in choice.lower():
            arena()
      
def start_isak():
      choice = input("""
You enter consciousness and look at your suroundings.
Dr.G: Now go left and win the Trial of Champions, it won't be too hard.
You: The what?!
DR.G: Don't worry just follow my instructions...
You see a path to the right and the left.
The left path seems to lead to a ancient arena.
The right path leads to some sort of shrine.
Where do you want to go:  """)
      if "left" in choice.lower():
        print("""
You enter what looks like an arena, like that from ancient greece.
Dr.G: You should see a arena now, do you see it?""")
        arena()
      if "right" in choice.lower():
            choice = input("""
Dr.G: NO! Don't go there. We don't know what will happen, you could DIE! Now turn back and continue on course.
Do you want to continue?:    """)
            if "yes" in choice.lower():
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
                  print(f"""
You now have {inventory} in your inventory.""")
                  print("""
De.G: Now go to The Arena, you lucky person... you really could have died!
You decide to go to back to where you woke up.""")
                  start_isak_2()
                  
            else:
                  print("You lost, bad luck... You shall die now!")
                  dead("not listening to the advice he was given")


#Programmet
print("""
You wake up on a plain hospital bed in a unfurnished room...
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




#START THEO

def Theo_game_intro():
      print("""
Dr. G: You are now in SCP-6969420-3. 
it seems to be a theater. 
Try to find the key and open the last door. """)


      print("""
A man: What are you doing, you need to get to the stage. 
There is only five minutes left before it starts. """)

      Follow = input("""
Dr. G: The entity seems to be safe, but I can't guarantee it. 
You can either follow him or you can try to get awey. """)
      
      if "follow" in Follow.lower():
            print("""
You continue to follow him and he pushes you on to a stage. 
You look on to the crowed and see houndreds of people. 
You take a secound look and see that the woman and men are 
copies of eachother and all of them have no face. """)
      
      else:
            print("""
You run away from the entity as fast as you can... """)
            dead = """
trying to run awey from the entity"""
            return dead
      
      dance = input("""
Dr. G: DANCE!!!! DANCE FOR FUCK SAKE!!!!!
IF TOU DON'T YOU WILL DIE: """)
      
      if "dance" in dance.lower():
            print("""
You start doing the macarena...
Suddenly you start hearing the macarena and everyone in the 
crowed stands up. 
You see all the entitys also starts doing the macarena. """)
      else:
            print("""
You stand there still in confusion and don't know what
to do. You see everyone standing up. """)
            dead = """
standing on stage and being eaten. """
            return dead
            
def The_room_of_many_rooms_and_other_stuff_it_also_have_an_exit_but_you_need_a_key_to_open_so_go_in_all_the_rooms_first_to_get_the_key():
      out = 1
      
      while out == 1:
            print("""
When you are done dancing you enter backstage. 
There you see 3 door (one to the left, one in the middle 
and one to the right), a mirror on the wall, a plant
in the corner. 
                  """)
            
            choice = input("""

                           """)      
      
