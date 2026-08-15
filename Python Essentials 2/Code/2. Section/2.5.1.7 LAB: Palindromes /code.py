def palindromeCheck(input_str):
    cleaned = ""
    for chr in input_str.lower():
        if chr.isalpha():
            cleaned += chr
    
    #print(cleaned)
    cleaned_reversed = "".join(list(cleaned)[::-1])
    #print(cleaned_reversed)
    if cleaned == cleaned_reversed:
        return True
    else:
        return False


input_str = input("Give a palindrome candidate: ")

print(palindromeCheck(input_str))
