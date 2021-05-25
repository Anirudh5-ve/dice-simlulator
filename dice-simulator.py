#  ------- DICE SIMULATOR ------

import random
print("DICE SIMULATOR")
print("CHOOSE YOUR OPTION")
print("1. ROLL\n2. EXIT")


def dice():
    number = random.randint(1,6)
    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")


while(True):
    a = input("ENTER YOUR CHOICE : ")
    if a == '1':
        dice()
    elif a == '2':
        print("Thank you for playing!")
        break
    else :
        print('INVALID INPUT\nCHOOSE BETWEEN 1 & 2')
        continue
    
