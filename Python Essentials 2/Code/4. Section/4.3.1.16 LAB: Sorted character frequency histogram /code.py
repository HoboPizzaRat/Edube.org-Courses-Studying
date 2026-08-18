#Scenario

# The previous code needs to be improved. It's okay, 
# but it has to be better.

# Your task is to make some amendments, which generate 
# the following results:

# 1. the output histogram will be sorted based on the 
# characters' frequency (the bigger counter should be 
# presented first)
# 2. the histogram should be sent to a file 
# with the same name as the input one, but with 
# the suffix '.hist' (it should be concatenated to 
# the original name)


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

for key, value in dict(sorted(histogram.items(), key=lambda item: item[1], reverse=True)).items():
    print(f"'{key}' has count {value}")

try:
    dst = open(f"{srcname}.hist", "wt")
    for key, value in dict(sorted(histogram.items(), key=lambda item: item[1], reverse=True)).items():
        dst.write(f"{key}: {value}\n")
    dst.close()
except IOError as e:
    print("Cannot write to the destination file: ", strerro(e.errno))
    exit(e.errno)
    
    
