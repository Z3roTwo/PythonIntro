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

memory = int(input("Value: "))
i = True
while i == True:
    try:
        operator = int(input("Choose operator [1] + [2] - [3] * [4] / [5] =: "))
        tal = int(input("Value: "))
    except ValueError:
        print("That's not a number... Please enter a real number next time.")

    if operator == 1:
        Summa = memory + tal
    elif operator == 2:
        Summa = memory - tal
    elif operator == 3:
        Summa = memory * tal
    elif operator == 4:
        Summa = memory / tal
    elif operator > 4:
        Summa = memory
        i = False
    memory = Summa

    print(Summa)