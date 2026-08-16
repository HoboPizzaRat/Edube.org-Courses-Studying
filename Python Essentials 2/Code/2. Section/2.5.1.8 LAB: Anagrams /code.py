print("This is anagram checker.")
text1 = input("Give text input1:")
text2 = input("Give text input2:")

def checkAnagram(text1, text2):

    def cleanInput(input):
        cleaned = ""
        for letter in input:
            if letter.isalpha():
                cleaned += letter
        return cleaned.lower()

    text1_cleaned = cleanInput(text1)
    text2_cleaned = cleanInput(text2)

    anagram_dict1 = {}
    for letter in text1_cleaned:
        if letter in anagram_dict1:
            anagram_dict1[letter] += 1
        else:
            anagram_dict1[letter] = 1

    anagram_dict2 = {}
    for letter in text2_cleaned:
        if letter in anagram_dict2:
            anagram_dict2[letter] += 1
        else:
            anagram_dict2[letter] = 1


    for key in anagram_dict1:
        if key in anagram_dict2 and anagram_dict1[key] == anagram_dict2[key]:
            pass
        else:
            return False

    for key in anagram_dict2:
        if key in anagram_dict2 and anagram_dict1[key] == anagram_dict2[key]:
            pass
        else:
            return False

    return True

result = checkAnagram(text1, text2)
print(result)