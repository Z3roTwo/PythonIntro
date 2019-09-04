# Variabler för namn, ålder etc.
restriction = "Welcome"
minimum = 18
firstName = input("Enter your firstname: ")
lastName = input("Enter your lastname: ")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a number... Please enter a real number this time.")


if age < minimum:
    restriction = "Begone thot"

print(restriction, firstName, lastName)