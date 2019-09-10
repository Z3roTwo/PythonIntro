#try:
#    tal1 = int(input("First Value: "))
#    operator = int(input("Choose operator [1] + [2] - [3] * [4] /: "))
#    tal2 = int(input("Second Value: "))
#except ValueError:
#    print("That's not a number... Please enter a real number next time.")
#
#if operator == 1:
#    Summa = tal1 + tal2
#elif operator == 2:
#    Summa = tal1 - tal2
#elif operator == 3:
#    Summa = tal1 * tal2
#elif operator == 4:
#    Summa = tal1 / tal2
#elif operator > 4:
#    Summa = "Choose a real operator"
#
#print(Summa)


#i = True
#number = 1
#tal = {}
#while i == True:
#   print(i)
#    try:
#        tal[number] = int(input("Value: "))
#        operator = int(input("Choose operator [1] + [2] - [3] * [4] / [5] =: "))
#    except ValueError:
#        print("That's not a number... Please enter a real number next time.")
#    number += 1
#
#    if operator == 1:
#        Summa = tal1 + tal2
#    elif operator == 2:
#        Summa = tal1 - tal2
#    elif operator == 3:
#        Summa = tal1 * tal2
#    elif operator == 4:
#        Summa = tal1 / tal2
#    elif operator > 4:
#        Summa = "Choose a real operator"
#        i = False
#
#    print(Summa)

#memory = int(input("Value: "))
#i = True
#while i == True:
#    try:
#        operator = int(input("Choose operator [1] + [2] - [3] * [4] / [5] =: "))
#        tal = int(input("Value: "))
#    except ValueError:
#        print("That's not a number... Please enter a real number next time.")
#
#    if operator == 1:
#        Summa = memory + tal
#   elif operator == 2:
#       Summa = memory - tal
#    elif operator == 3:
#       Summa = memory * tal
#    elif operator == 4:
#       Summa = memory / tal
#   elif operator > 4:
#       Summa = memory
#        i = False
#    memory = Summa
#
#    print(Summa)

memory = int(input("Memory: ")) # första siffran
prev = [0, 3, 0] # sparar föregående uträkning för att få gånger och delat att fungera på rätt sätt
tal = 0 # bara för att hålla alla variabler vid toppen
operator = 0 # bara för att hålla alla variabler vid toppen
summa = 0 # bara för att hålla alla variabler vid toppen
new = 0 # bara för att hålla alla variabler vid toppen
loop = True # så länge den är true så fortsätter den fråga efter nya tal

while loop == True:
    try:
        operator = int(input("Choose operator [1] + [2] - [3] * [4] / [5] =: "))
        tal = int(input("Value: "))
    except ValueError:
        print("That's not a number... Please enter a real number next time.")

    if operator == 3:

        if prev[1] == 1:
            new = prev[2] * tal
            summa = prev[0] + new
        elif prev[1] == 2:
            new = prev[2] * tal
            summa = prev[0] - new
        elif prev[1] == 3:
            summa = memory * tal
        elif prev[1] == 4:
            new = prev[2] * tal
            summa = prev[0] / new

    elif operator == 4:

        if prev[1] == 1:
            new = prev[2] / tal
            summa = prev[0] + new
        elif prev[1] == 2:
            new = prev[2] / tal
            summa = prev[0] - new
        elif prev[1] == 3:
            summa = memory / tal
        elif prev[1] == 4:
            summa = memory / tal

    elif operator == 1:
        summa = memory + tal
    elif operator == 2:
        summa = memory - tal
    elif operator < 1 or operator > 4:
        summa = memory
        loop = False

    prev[0] = memory
    prev[1] = operator
    prev[2] = tal
    memory = summa

    print(summa)