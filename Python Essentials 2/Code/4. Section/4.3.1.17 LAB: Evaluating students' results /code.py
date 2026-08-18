
# Your task is to write a program which:

# 1. asks the user for Prof. Jekyll's file name;
# 2. reads the file contents and counts the 
# sum of the received points for each student;
# 3. prints a simple (but sorted) report, 
# just like this one:

# the format of the students scores are 
# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5

# raise own errors if the files dont cant open 
# or contain all the values
from os import strerror

class ScoreDataException(Exception):
    def __init__(self, message, errocode):
        super().__init__(self, message)
        self.errorcode = errocode

student_scores = {}
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, "rt")
except Exception as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, "wt")
except Exception as e:
    print("Cannot open the dest file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

studentTotalScores = {}
for line in src.readlines():
    try:
        #print(line)
        items = line.strip().split("\t")
        firstname = items[0].strip().lower()
        lastname = items[1].strip().lower()
        score = float(items[2].strip())
        #print(firstname, lastname, score)
        if firstname == None or lastname == None or score == None:
            raise ScoreDataException("Invalid datarow", 404)
        key = f"{firstname} {lastname}"
        if key in studentTotalScores:
            studentTotalScores[key] += score
        else: 
            studentTotalScores[key] = score
    except ScoreDataException as e:
        print(strerror(e.errno), e.errorcode)
    except Exception as e:
        print("Error that just occured. I have no idea how this woudl execute")

for key, value in dict(sorted(studentTotalScores.items(), key=lambda item: item[1], reverse=True)).items():
    print(f"{key.ljust(20, ' ')}: {str(value)}")

try:
    dst = open(f"{dstname}", "wt")
    for key, value in dict(sorted(studentTotalScores.items(), key=lambda item: item[1], reverse=True)).items():
        dst.write(f"{key.ljust(20, ' ')}: {str(value)}\n")
except IOError as e:
    print("Cannot write to the destination file: ", strerror(e.errno))
    exit(e.errno)

finally:
    src.close()
    dst.close()