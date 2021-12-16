items = ["sword of smiting", "fist"]
inventory = []
inventory.append(items[1])
player_hp = 100

#template för varelser, först i listan är HP sen DMG sen namn
rat = [10, 1, "Rat"]
skeleton = [15, 2, "Skeleton"]
troll = [30, 2, "Troll"]
archer = [5, 4, "Archer"]

#namnet är bara namnet på vapnet men numret efter är skada
weapon = {
    "fist": 1,
    "sword of smiting": 4 ,
    "iron sword": 2,
}

def dead(dead):
    print(f"Dr. G: The D class died while {dead}. ")
    exit()

def inv():
    print(f"You open your bag and find:  {inventory}")


#ATTACK system: argumentet är bara en av varelsena. Allt detta skrevs av mig//MVH Isak
def attack(creature):
    global player_hp
    creature_name = creature[2]
    creature_hp = creature[0]
    print(f"You are fighting a {creature_name}!")
    choise = (input(f"You have {inventory} in your inventory. Chose a weapon: use only singular:    "))
    choise = choise.lower()
    weapon_local = weapon[choise]
    creature_dmg = creature[1]
    while True:
        if player_hp >= 1:
            if creature_hp >= 1:
                player_hp = player_hp - creature_dmg
                creature_hp = creature_hp - weapon_local
                print(f"You did {weapon[choise]} dmg, the {creature_name} has {creature_hp}HP left!")
                print(f"The {creature_name} attacks you and does {creature_dmg} you have {player_hp}HP left!")
            else:
                print("You won!")
                return()
        else:
            dead(f"fighting a {creature_name}")
