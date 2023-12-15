test_1 = "Guðni Th"


#for(character in test_1):

if all(character.isalpha() for character in test_1 if character == " "):
    print(False)
