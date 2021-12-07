inventory = []


def inv():
    print(f"You open your bag and find:  {inventory}")
    
def attack(creature, weapon):
    creature_hp = creature[0]
    creature_hp_new = creature_hp - weapon
    print(f"You did {weapon} dmg, the {creature} has {creature_hp_new}HP left!")