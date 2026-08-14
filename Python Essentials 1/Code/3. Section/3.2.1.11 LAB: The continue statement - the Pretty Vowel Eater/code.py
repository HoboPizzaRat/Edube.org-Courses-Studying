# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("gimme word: ")

for letter in user_word.upper():
    # Complete the body of the for loop.
    if letter in "IOUEA":
        continue
    else:
        print(letter, end="")