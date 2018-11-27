from sys import exit

pts = 3

def create_character():
    print("***********************************************")
    print("Welcome to the Dungeon!\nPlease create your character by answering these questions.")
    name = input("Name?> ")
    print(f"Hello {name}, so good of you to join!")
    print("You will now choose your stats.")
    print(" You have 3 points to put in one of these skills: ")
    print("Strength -- Which determines how good you are at fighting.")
    print("Agility -- Which determines how good you are at sneaking.")
    print("Mind -- Which determines how good you are at talking.")

number = input("Number: ")

def is_int(num):
    numToCheck = int(num)
    if numToCheck / 1 == int(num):
        print(numToCheck)
        print(num)
        print("True")
        return True
    else:
        print(numToCheck)
        print(num)
        print("False")
        return False

is_int(number)
