first = "Hello World"

# This is a comment

print("I AM A COMPUTER!")

if 1 < 2 and 4 > 2:
    print("Math is fun")

nope = None

result = True and False

lenght = len("What's my length?")

upcase = "i am shouting".upper()

thousandString = "1000"

thousandNumber = int(thousandString)

combinePhrase = str(4)+"real"

print(3*"cool")

#print(1/0)
print("ZeroDivisionError: division by zero")

myList = []

print(type(myList))

#name = input("Mettez votre nom bande de batard!")


while True:
    try:
        number = int(input("Un nombre n'importe lequel!"))
        break
    except ValueError:
        print("C'est pas un nombre!")

if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

fruit = "apple"

print(fruit[1])

print("y" in "xylophone")

my_String = "aaaaa"

if my_String.islower():
    print("True")
else:
    print("False")
    