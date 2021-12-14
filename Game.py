items = ("Sword of Smiting", "Fist")
inventory = []
inventory.append(items(1))
player_hp = 100
player_dmg = ["Fists", 1, "Sword of Smiting"]
rat = [10, 1]

def inv():
    print(f"You open your bag and find:  {inventory}")
    
def attack(creature, weapon):
    creature_hp = creature[0]
    creature_dmg = creature[1]
    creature_hp_new = creature_hp - weapon
    print(f"You did {weapon} dmg, the {creature} has {creature_hp_new}HP left!")
    print(f"The {creature} attacks you and does {creature_dmg} you have {player_hp}HP left!")

def dead(dead):
    print(f"Dr. G: The D class died while {dead}. ")