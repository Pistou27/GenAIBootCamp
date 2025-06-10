def word_dictionnary(word):
    result = {}
    for index, letter in enumerate(word):
        if letter not in result:
            result[letter] = []
        result[letter].append(index)
    return result

word_entry = input("Entrez un mot n'importe lequel ---> ").strip()

print(word_dictionnary(word_entry))

