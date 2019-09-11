# Slump generator

import random, time                                     # Importera de mudoler som behövs

oof = True                                              # För att kunna stoppa loopen sen
count = 3                                               # För att printa "Rolling..." 3x

print("Welcome!")                                       # Hälsa användaren välkommen

while oof == True:                                      # Starta loopen
    try:                                                # För att fånga problem
        meny = input("[A] Start, [S] Stop: ")           # Fråga om den vill starta programmet
        print("\033[H\033[J")                           # "Rensa" Terminalen

        if meny.lower() == "a":                         # Gör detta om den väljer a
            sides = int(input("How many sides?: "))
            if sides == 0:                              # Om Användaren väljer 0 sider defaultar den till 1
                sides = 1
            number = random.randint(1, sides)           # 
            while count > 0:
                print("Rolling...")
                count -= 1
                time.sleep(1)
            count = 3
            print(number)
        elif meny != "a":
            oof = False
            print("GoodBye Bish")
    except:
        print("Please enter a number this time!")