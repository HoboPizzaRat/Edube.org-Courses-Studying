input_string = input("Give a input: ")

def askValidInputShift():
    input_shift = 0
    
    while(True):
        try: 
            input_shift = int(input("Give shift(1-25): "))
            if input_shift >= 1 and input_shift <= 25:
                return input_shift
        except:
            print("Wrong input! Give value between 1-25: ")


input_shift = askValidInputShift()

def caesarCipher(input_string, input_shift):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "abcdefghijklmnopqrstuvwxyz".upper()
    output = ""
    for chr in input_string:
        chr_shifted = ""
        if chr in lowercase:
            chr_shifted = lowercase[(lowercase.index(chr)+input_shift)%len(lowercase)]
        elif chr in uppercase:
            chr_shifted = uppercase[(uppercase.index(chr)+input_shift)%len(uppercase)]
        else:
            chr_shifted = chr
            
        output += chr_shifted
        
    return output
            
ciphered = caesarCipher(input_string, input_shift)
print(ciphered)