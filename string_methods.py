#A string is a list of characters
sentence = "The quick brown fox jumps over the lazy dog."

print(sentence[7])

#loop through string
for character in sentence:
        print(character)

print()
for index in range(len(sentence)):
    print(sentence[index])
    if sentence[index].isalnum():
        print(True)
    else
         print(False)