def mysplit(strng):
    wordlist = []
    word = ""
    for chr in strng.strip():
        if chr.isspace():
            wordlist.append(word)
            word = ""
        else:
            word += chr
            
    if word != "":
        wordlist.append(word)
    
    return wordlist


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
