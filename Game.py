items = ["sword of smiting", "fist"]
inventory = []
inventory.append(items[1])
player_hp = 100
player_dmg = ["Fists", 1, "Sword of Smiting"]
rat = [10, 1]
weapon = {
    "fist": 1,
    "Sword of smiting":4 
}

def inv():
    print(f"You open your bag and find:  {inventory}")
    
def attack(creature):
    creature_hp = creature_hp = creature[0]
    choise = int(input(f"You have {inventory} in your inventory. Use numbers to chose a weapon... count from the start!"))
    choise-=1
    weapon_local = weapon[inventory[choise]]
    creature_dmg = creature[1]
    while True:
        if creature_hp >= 1:
            creature_hp = creature_hp - weapon_local
            print(f"You did {weapon} dmg, the {creature} has {creature_hp}HP left!")
            print(f"The {creature} attacks you and does {creature_dmg} you have {player_hp}HP left!")
        else:
            print("You won!")
            return()
        
def dead(dead):
    print(f"Dr. G: The D class died while {dead}. ")