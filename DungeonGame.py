from sys import exit

linebr = "**************************************************"

class Character(object):
    inv = []
    def __init__(self, name, strength, agility, mind):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.mind = mind

class Item(object):
    def __init__(self, itemName, stat, effect):
        self.itemName = itemName
        self.stat = stat
        self.effect = effect

def addToInv(item):
    i = item
    character.inv.append(i)

    stat = i.stat
    effect = i.effect

    if stat == character.strength:
        character.strength += effect
    elif stat == character.agility:
        character.agility += effect
    elif stat == character.mind:
        character.mind += effect
    else:
        print("Something went wrong")

def create_item(name, stat, effect):
    iName = name
    iStat = stat
    iEffect = effect
    return Item(iName, iStat, iEffect)

def getInput(prompt):
    getPrompt = prompt
    while True:
        try:
            data = int(input(prompt))
            break
        except ValueError:
            print("Oops, not a number, try again.")

    return data

def getCommand(prompt, character):
    getPrompt = prompt
    thisChar = character

    while True:
        try:
            data = int(input(prompt))
            break
        except ValueError:
            print("Oops, not a number, try again.")

    if data == 0:
        print(f"Name:      {thisChar.name}")
        print(f"Strength:  {thisChar.strength}")
        print(f"Agility:   {thisChar.agility}")
        print(f"Mind:      {thisChar.mind}")
        print("Items in Inventory:")
        for i in thisChar.inv:
            print(i.itemName, sep = "\n")
        print(linebr)


    return data

def create_character(points):
    pts = points
    print(linebr)
    print("Welcome to the Dungeon!\nPlease create your character by answering these questions.")
    name = input("Name?> ")
    print()
    print(f"Hello {name}, so good of you to join!")
    print()
    print("You will now choose your stats.")
    print()
    print("You have 3 points to put in one of these skills: ")
    print("Strength -- Determines your skill at fighting.")
    print("Agility  -- Determines your skill at sneaking.")
    print("Mind     -- Determines your skill at talking.")
    print(linebr)
    print(" ")
    print(f"You have {pts} points remaining.")

    while True:
        strength = getInput("Strength(0-3): ")
        if strength > pts:
            print("Not enough points, try again.")
        else:
            pts = pts - strength
            break

    print(f"You have {pts} points remaining.")

    while True:
        agility = getInput("Agility(0-3): ")
        if agility > pts:
            print("Not enough points, try again.")
        else:
            pts = pts - agility
            break

    print(f"You have {pts} remaining.")

    while True:
        mind = getInput("Mind(0-3): ")
        if mind > pts:
            print("Not enough points, try again.")
        else:
            pts = pts - mind
            break

    print(linebr)
    print(f"Well done {name}, you have:")
    print(f"{strength} point(s) in Strength.")
    print(f"{agility} point(s) in Agility.")
    print(f"{mind} point(s) in Mind.")
    print()
    print("To access your stats at anytime, type the command '0'")

    return Character(name, strength, agility, mind)

def prisonCell(character):
    thisChar = character
    print(linebr)
    notEscaped = True
    while notEscaped:
        #run the room
        print("You've been in King Cragfist's prison for two weeks now,
        print("accused of a crime you didn't commit.")
        print()
        print("Your cell is made of iron bars, too strong for you to break. You've tried.")
        print("There are two more empty cells to either side of you.")
        print("A solitary guard, armed with a sword and shield, snores in a chair just outside the iron bars.")
        print("The key to your cell hangs on a ring off the guard's belt loop, just barely out of reach.")
        print()
        print("1. Wake up the guard.)
        print("2. ")
        command = getCommand("Please enter a command >> ", thisChar)
        if command == 1:
            notEscaped = False

    print("You escaped the prison")
    print(linebr)



character = create_character(3)
prisonCell(character)
