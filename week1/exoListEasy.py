#1
values = [1, 2, 3, 4]

for val in values:
    print(val)

#2
for val in values:
    print(val*20)

#3
names = ["Elie", "Tim", "Matt"]
firsletter = []

for name in names:
    firsletter.append(name[0])
print (firsletter)

#4
values2 = [1, 2, 3, 4, 5, 6]
valuesWhitoutImpair = []
for num in values2:
    if num % 2 == 0:
        valuesWhitoutImpair.append(num)
print(valuesWhitoutImpair)
#Deuxième façon comme exemple
valuesWhitoutImpair2 = [x for x in values2 if x % 2 == 0]
print(valuesWhitoutImpair2)

#5
firstList = [1, 2, 3, 4]
secondList = [3, 4, 5, 6]
common = list(set(firstList).intersection(set(secondList)))
print(common)

#6
lowerReverse = [name[::-1].lower() for name in names]
print (lowerReverse)

#7
wordFirst = "first"
wordThird = "third"
common2 = list(set(wordFirst).intersection(set(wordThird)))
print(common2)

#8
divBy12 = [num for num in range(1, 101) if num % 12 == 0]
print(divBy12)

#9
wordAmazing = "amazing"
vowel = ["a","e","i","o","u","y"]
listMzing = [con for con in wordAmazing if con not in vowel]
print (listMzing)

#10
listInList3 = [[i for i in range(0, 3)] for _ in range(0, 3)]
print(listInList3)

#11
listInList10 = [[i for i in range(0, 10)] for _ in range(0, 10)]
print(listInList10)