#1

listEntry = [("name", "Elie"), ("job", "Instructor")]
dictEntry = dict(listEntry)
print(dictEntry)

#2

listAcronyme = ["CA", "NJ", "RI"]
listStatename = ["California", "New Jersey", "Rhode Island"]

dictAcroState = dict(zip(listAcronyme, listStatename))
print(dictAcroState)

#3

listvowel = ["a", "e", "i", "o", "u", "y"]
dictvowel = {vowel: 0 for vowel in listvowel}
print (dictvowel)

#4

listAlphabet = []
for num in range(65,91):
    listAlphabet.append(chr(num))

dictAlphabet = {}

for i in range(len(listAlphabet)):
    dictAlphabet[i+1] = listAlphabet[i]

print(dictAlphabet)

#Super bonus

wordEntry = "awesome sauce"
#On utililise exo 3

for letter in wordEntry:
    if letter in dictvowel:
        dictvowel[letter] +=1

print (dictvowel)