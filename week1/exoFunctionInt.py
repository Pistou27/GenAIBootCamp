#1
def find_largest(listNbr : list):
    #déclaration du plus petit nombre possible
    maxNbr = float('-inf')
    for nbr in listNbr:
        if nbr > maxNbr:
            maxNbr = nbr
    return maxNbr

#2
def check_letter(word, letter):
    return letter in word

#3
#Par contre je suis parti sur que les nombres entiers positifs, les nombres négatifs ne sont pas compris dedant
def count_to_number(nbr: int):
    for nm in range(1, nbr + 1):
        print(nm)

#4

