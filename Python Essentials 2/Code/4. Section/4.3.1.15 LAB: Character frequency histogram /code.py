#Scenario

# A text file contains some text (nothing unusual) 
# but we need to know how often (or how rare) each 
# letter appears in the text. Such an analysis may 
# be useful in cryptography, so we want to be able 
# to do that in reference to the Latin alphabet.

# Your task is to write a program which:

# 1.asks the user for the input file's name;
# 2.reads the file (if possible) and counts all the Latin 
# letters (lower- and upper-case letters are treated as equal)
# 3.prints a simple histogram in alphabetical order 
# (only non-zero counts should be presented)

# open file, throw error if no cannot open the file
from os import strerror
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, "rt")
except IOError as e:
    print("Cannot open the source file: ",strerror(e.e))
    exit(e.errno)

buffersize = 4096
histogram = {}
# read the buffer in sections and put the characters into histogram.
try:
    while True:
        buffer = src.read(buffersize)
        if not buffer:
            break

        for chr in buffer:
            if chr.isalpha():
                character = chr.lower()
                if character in histogram:
                    histogram[character] += 1
                else:
                    histogram[character] = 1
            else:
                continue
    src.close()
except IOError as e:
    print("cannot read the source file for some reason")
    exit(e.errno)

for key, value in dict(sorted(histogram.items())).items():
    print(f"'{key}' has count {value}")



    
