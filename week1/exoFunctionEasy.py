#1
def add_two_numbers(num1, num2):
    return num1 + num2

#2
def greet(name):
    print(f"Hello, {name}!")

#3
def check_even_odd(num: int):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

#4
#Mais en vrai on peut utiliser la fonction sum
def sum_list(numbers: list):
    total = 0
    for number in numbers:
        total += number
    return total
 
# def sum_list2(numbers):
#     return sum(numbers)

#5
def print_days():
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in week : print(day)

#6
def check_sign(number : int):
    if number > 0 : print("Positive")
    elif number < 0 : print("Negative")
    else : print("Zero")

#7
def repeat_word(word: str, nbr: int):
    for _ in range(nbr): print(word)

