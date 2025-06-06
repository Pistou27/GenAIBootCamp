#Challenge 1

def iterableForNumber(number, lenght):
    listresult = [number * x for x in range(1, lenght + 1)]
    print(listresult)

iterableForNumber(5, 10)

#Challenge 2

def removeDuplicateCharacteres(word):
    if not word:
        return ""
    result = word[0]
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            result += word[i]
    
    print(result)

removeDuplicateCharacteres("cccccaarrrbbon")