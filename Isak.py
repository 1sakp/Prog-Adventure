from Game import *

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
      if "sword" or "upgrade" in choise.lower():
            weapon["sword of smiting"] += 2
      attack(rat)
            
      
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
          You see a path to the right and the left.
          Dr.G: Now go left and win the Trial of Champions, it won't be too hard.
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



start_isak()