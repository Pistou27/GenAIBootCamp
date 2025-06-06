#Exercise 1 : Outputs

# >>> 3 <= 3 < 9 True

# >>> 3 == 3 == 3 True

# >>> bool(0) False

# >>> bool(5 == "5") False

# >>> bool(4 == 4) == bool("4" == "4") True

# >>> bool(bool(None)) False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

#x is True
print("x is", x)
#y is False
print("y is", y)
#a:5
print("a:", a)
#b:10
print("b:", b)

#Exercise 2 : Longest word without a specific character
longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the character 'A' (or type 'quit' to stop): ")

    if sentence.lower() == "quit":
        print("Thanks for playing!")
        break

    # Check if 'a' or 'A' is in the sentence
    if 'a' in sentence.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again.")
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You set a new longest sentence without 'A'.")
    else:
        print("Try again to beat the longest sentence!")

#Exercise 3: Working on a paragraph


