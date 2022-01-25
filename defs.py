
#variabler
from email.quoprimime import body_check


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
    elif "right" in choice_1.lower() or "graveyard" in choice_1.lower():
        graveyard()
    elif "behind" in choice_1.lower() or "gate" in choice_1.lower():
        gate()
    elif "mansion" in choice_1.lower():
        door()
    elif "window" in choice_1.lower():
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
    elif "shed" in choice_graveyard.lower():
        shed()
    elif "grave" in choice_graveyard.lower() or "graves" in choice_graveyard.lower():
        graves()

def graves():
    choice_graves = int(input("""There are four graves which do you want to examine?"""))
    if 1 in choice_graves:
        print()
    elif 2 in choice_graves:
        print()
    elif 3 in choice_graves:
        print()
    elif 4 in choice_graves:
        print()

def shed():
    choice_shed = input("""You go up to the shed and push the door, it creaks open.
Do you go in?""")
    if "yes" in choice_shed.lower() or "enter" in choice_shed.lower():
        inside_shed()
    elif "no" in choice_shed.lower() or "leave" in choice_shed.lower():
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
    if "dig" in choice_tree.lower() or "yes" in choice_tree.lower():
        print()
    elif "no" in choice_tree.lower() or "leave" in choice_tree.lower():
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
    if "yes" in choice_well.lower() or "down" in choice_well.lower():
        well_bottom()
<<<<<<< HEAD
    elif "no" in choice_well.lower() or "leave" in choice_well.lower():
        starting_point()
=======
    elif "no" or "leave" in choice_well.lower():
        starting_pmoint()
>>>>>>> b36c9b255b0b175dc9e2fbfd5e00a835cb143793

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
    elif player_hp >= 25:
        print("You are victorious with grave injuries.")
        dungeon()
    elif player_hp >= 50:
        print("You win with minor inconvinences.")
        dungeon()
    elif player_hp >= 75:
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
    if "yes" in choice_mansion.lower() or "attic" in choice_mansion.lower():
        attic()
    elif "no" in choice_mansion.lower() or "leave" in choice_mansion.lower():
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
    elif player_hp >= 25:
        print("You are victorious with grave injuries.")
    elif player_hp >= 50:
        print("You win with minor inconvinences.")
    elif player_hp >= 75:
        print("You call this a challenge? Hah.")

#if you knock too much you get killed lmao, 
def door():
    choice_door = input("""The mansion door is giant, you try to open the door but it is closed and will not budge.
Will you try to knock the door?""")
    knock_count = 0
    while knock_count <= 3:
        if knock_count == 3:
            dead("for being too curious.")
        if "yes" in choice_door.lower() or "knock" in choice_door.lower():
            choice_knock = ("Do you knock again?")
            if "knock" in choice_knock.lower() or "yes" in choice_knock.lower():
                knock_count = knock_count + 1 
        elif "no" in choice_door.lower() or "leave" in choice_door.lower():
            starting_point()


def window():
    choice_window = input("""You look through the window and see a dark room, the room seems empty. 
Do you enter or do you leave?""")
    if "leave" in choice_window.lower() or "back" in choice_window.lower():
        starting_point()
    elif "enter" in choice_window.lower() or "go in" in choice_window.lower():
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
      if "take" in choice.lower() or "grab" in choice.lower() or "book" in choice.lower():
            print("""
You wake up in the hospital bed again""")
            Theo_game_intro()
      elif "exit" in choice.lower() or "leave" in choice.lower():
            arena_corridor()

def arena_corridor():
      choice = input("""
You enter a corridor with 3 rooms, one on the left, one on the right and one in the middle:  what door do you wish to enter? :   """)
      if "right" in choice.lower():
            arena_door_right()
      if "left" in choice.lower():
            arena_door_left()
      if "middle" in choice.lower() or "center" in choice.lower():
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

#defen är bara masa text med typ en eller två val. Bara ett intro till delen
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
    
#Theos main spel i de stora spelet 
def The_room_of_many_rooms_and_other_stuff_it_also_have_an_exit_but_you_need_a_key_to_open_so_go_in_all_the_rooms_first_to_get_the_key():
        out = 1
        l_red_card = 0
        m_blue_card = 0
        r_green_card = 0
        done_room_1 = 0
        done_room_2 = 0
        key_1 = 0
        print("""
When you are done dancing you enter backstage. """)

        while out == 1:
            print("""
You see 3 door (one to the left, one in the middle and 
one to the right), a mirror on the wall, a plant in the
corner. """)
            
            choice_go_questionmark = input("""
Dr. G: You should do somthing. You can't just stand there. """)
            room_1 = 1
            room_2 = 1
            
#när man går till mirror. man kan för röt kort och när man tar de ändras stället. 
#innan man tar kort
            if "mirror" in choice_go_questionmark.lower() and l_red_card == 0:
                take_stuff = input("""
You walk up to the mirror and see you yourself in a large 
white room. You looka at it for a while and then you see 
what looks like a red card sticking out from the side of 
the mirror. """)
                if "take" in take_stuff.lower() or "card" in take_stuff.lower() or "grab" in take_stuff.lower():
                    l_red_card = 1
                    print("""
You look a little closer and see its a red key-card. You 
take the card and look at the mirror agian. But once you 
look you see that the reflection is gone. """)
                    print("""
Dr. G: You have a keycard so try to open one of the doors, 
or you could you can just stand there. """)
                
                elif "leave" in take_stuff.lower() or "go" in take_stuff.lower():
                    print("""
you leave the mirror and look at the room agian. """)
                
                else:
                    print("""
Again. """)

#efrter man tar kort
            elif "mirror" in choice_go_questionmark.lower() and l_red_card == 1:
                take_stuff = input("""
You walk up to the mirror agoin and once agian you see
no reflection. You look at it for a while and the go 
away to do other stuff. """)

#när man går till plantan inget händer man bara går dit och tillbaka
            elif "plant" in choice_go_questionmark.lower() or "corner" in choice_go_questionmark.lower():
                print("""
You walk up to the plat look at it for for to long and 
then you walk away. """)

#de vänstra römet änras om man har de röda kortet eller inte
#utan de röda kortet
            elif "left" in choice_go_questionmark.lower() and l_red_card == 0:
                print("""
You walk up to the door on the left. You try to open it 
but it won't open. you look around and se a red box where
you cand place a card. You dicide to walk awey. """)
            
#med de röda kortet
            elif "left" in choice_go_questionmark.lower() and l_red_card == 1 and done_room_1 == 0:
                first = 1
                chair_broke = 0
                
                if room_1 == 1:
                    print("""
You open the door at the left and enter. """)
                    room_1 = 0
                
                #får olika utskrifter om man har sat sig på stolen eller inte
                if chair_broke == 0:
                    print("""
When you look around you see a box on a table in front 
of you and a chair on the other side. """)
                else:
                    print("""
When you look around you see a box on a table in front 
of you and a broken chair on the other side. """)
                
                #man väljer vad man ska göra 
                while 1 == first:
                    box2_t = 1
                    box_xox = input("""
Dr. G: Don't just stand there do something. """)
                    
                    #om man väljer att ta upp lådan första puslet
                    if "box" in box_xox.lower() or "take" in box_xox.lower():
                        print("""
you look at the box and see a note and a keybad. On the 
are ones and zeros and it goes. 

0010
0001
1001
0110 """)
                        while 1 == box2_t:
                            code_room_l_red = int(input("""
Put in the code: """))
                            if code_room_l_red == 2196:
                                print("""
You open the box slowly and inside you see a blue keycard. 
You take ta card and the leave the room. """)
                                m_blue_card = 1
                                box2_t = 0
                                first = 0
                                done_room_1 = 1
                            
                            else:
                                print("""
Wrong, try agian. """)
                    
                    #om man väljer att säta sig på stolen
                    elif "sit" in box_xox.lower() or "chair" in box_xox.lower():
                        print("""
You sit on the chair and after a wile you hear it crack. 
After a while the chair brakes and you fall on the floor,
after you fell you try to stand upp as fast as you can. """)
                        chair_broke = 1
                    
                    #om man lämnar rumet
                    elif "leave" in box_xox.lower() or "go" in box_xox.lower():
                        print("""
You leave the room where the box is. """)
                        first = 0
                        
            elif "left" in choice_go_questionmark.lower() and l_red_card == 1 and done_room_1 == 1:
                print("""
You walk up to the door on the left but when you get close 
it dissapers. you stand there wondering what happened and 
after a while you walk awey, then you see the door apper 
again. """)
            
#mitten rumet man behöver de blåa kortet
#utran de blåa kortet
            elif "middle" in choice_go_questionmark.lower() and m_blue_card == 0:
                print("""
You walk up to the door in the middle. You try to open it 
but it won't open. you look around and se a blue box where
you cand place a card. You dicide to walk awey. """)
            
#när du har de blåa kortet
            elif "middle" in choice_go_questionmark.lower() and m_blue_card == 1 and done_room_2 == 0:
                no_go = 1
                if room_2 == 1:
                    print("""
You enter the room in the middle. """)
                    room_2 = 0
                   
                   #väljer om puzel eller gå
                puzzle_or_not = input("""
You see a long room and at the end of it you see a bunch 
of lines. 
You walk closer and you see another keybad. 
Dr. G: what are you doing look closer or you can just leave. """)

                while 1 == no_go:
                    #om man tog puzzle
                    if "closer" in puzzle_or_not.lower():
                        iamman = 1
                        print("""
when youi walk closer you see. 

/|||/ + V
V|| + ||||
/|||/||| + |X
|| + ||""")
                        while 1 == iamman:
                            code_i_dont_like_this_i_couldnt_do_what_i_wanted = int(input("""
Figure out the code and out it in: """))
                            
                            if code_i_dont_like_this_i_couldnt_do_what_i_wanted == 1011174:
                                print("""
You hear a sound behind you. you look around and see a green 
card on the ground. You pick the card and walk out. """)
                                iamman = 0
                                no_go = 0
                                done_room_2 = 1
                                r_green_card = 1
                        
                            else:
                                print("""
Wrong, try agian. """)
                            
                    elif "leave" in puzzle_or_not.lower() or "go" in puzzle_or_not.lower():
                        print("""
You leave the room for some reson. """)
                        no_go = 0
                    
                    else:
                        print("""
Agian. """)

            elif "middle" in choice_go_questionmark.lower() and m_blue_card == 1 and done_room_2 == 1:
                print("""
You walk up to the door in the middle but when you get close 
it dissapers. you stand there wondering what happened and 
after a while you walk awey, then you see the door apper 
again. """)
                        
#högra rummet bhöver gröna kortet
#utan görn kort
            elif "right" in choice_go_questionmark.lower() and r_green_card == 0:
                print("""
You walk up to the door at the right. You try to open it 
but it won't open. you look around and se a green box where
you cand place a card. You dicide to walk awey. """)
            
            elif "right" in choice_go_questionmark.lower() and r_green_card == 1:
                print("""
You open the door and walk in. when you walk through the door
you walk into a brick wall. you take a few steps back and 
inspect the wall. When you do that you see a key in the wall and 
you take it. """)
                print("""
you stand there a little bit more to look at the wall and then
you walk away. """)
                key_1 = 1
            
            elif "exit" in choice_go_questionmark.lower() and key_1 == 0:
                print("""
You start walking to the exit. 

Dr. G: NOOOOOOOOOO! Don't go there. You can't right now. Please. 
Don't do it. You just can't. """)
                
            elif "exit" in choice_go_questionmark.lower() and key_1 == 1: 
                print("""
You start to walk to the exit. 

Dr. G: Well done D-class, you are soon done. 

You but in the key and walk out the door. Then all of a sudden you
you fall a sleep. """)
                out = 0
            
            else:
                print("""
again. 
                      """)