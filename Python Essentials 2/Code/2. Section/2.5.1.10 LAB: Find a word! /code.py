print("This is a checker that checks whether the characters comprising the first string hidden inside the second string?.")
text1 = input("Give text input1:")
text2 = input("Give text input2:")

def checkStringHidden(text1, text2):

    def cleanInput(input):
        cleaned = ""
        for letter in input:
            if letter.isalpha():
                cleaned += letter
        return cleaned.lower()

    text1_cleaned = cleanInput(text1)
    text2_cleaned = cleanInput(text2)

    hidden_dict1 = {}
    for letter in text1_cleaned:
        if letter in hidden_dict1:
            hidden_dict1[letter] += 1
        else:
            hidden_dict1[letter] = 1

    hidden_dict2 = {}
    for letter in text2_cleaned:
        if letter in hidden_dict2:
            hidden_dict2[letter] += 1
        else:
            hidden_dict2[letter] = 1


    for key in hidden_dict1:
        if key in hidden_dict2 and hidden_dict1[key] <= hidden_dict2[key]:
            pass
        else:
            return False

    return True

result = checkStringHidden(text1, text2)
print(result)