from sys import exit

linebr = "**************************************************"

class Character(object):

    inv = []

    def __init__(self, name, strength, agility, mind):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.mind = mind


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
        print(*thisChar.inv, sep = "\n")
        print(linebr)


    return data

def create_character(points):
    pts = points
    print(linebr)
    print("Welcome to the Dungeon!\nPlease create your character by answering these questions.")
    name = input("Name?> ")
    print()
    print(f"Hello {name}, so good of you to join!")
    print("You will now choose your stats.")
    print("You have 3 points to put in one of these skills: ")
    print("Strength -- Which determines how good you are at fighting.")
    print("Agility  -- Which determines how good you are at sneaking.")
    print("Mind     -- Which determines how good you are at talking.")
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
    print("")
    print("To access your stats at anytime, type the command '0'")

    return Character(name, strength, agility, mind)

def prisonCell(character):
    thisChar = character
    print(linebr)
    notEscaped = True
    while notEscaped:
        #run the room
        command = getCommand("You're in a prison, how do you proceed? >> ", thisChar)
        if command == 1:
            notEscaped = False

    print("You escaped the prison")
    print(linebr)



character = create_character(3)
character.inv.append("sword")
character.inv.append("shield")

prisonCell(character)
