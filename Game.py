inventory = []


def inv():
    print(f"You open your bag and find:  {inventory}")
    
def attack(creature, weapon):
    creature_hp = creature - weapon
    print(f"You did {weapon} dmg, the {creature} has {creature_hp}HP left!")