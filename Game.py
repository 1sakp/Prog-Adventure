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

#START
#Såhär kör man en annan fil... MVH:Isak
exec(open("Isak.py").read())