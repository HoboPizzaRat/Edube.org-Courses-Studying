import os
import sys
import itertools
import shutil

def recursiveSearchOnPath(path="./tree", search="python"):
    foundDirectories = []
    startpath = path
    for item in os.listdir(startpath):
        item_wholepath = startpath+"/"+item
        #print(item_wholepath)
        if not os.path.isdir(item_wholepath):
            return [item_wholepath]
        
        if os.path.isdir(item_wholepath):
            #print("Doing recursive stuff")
            foundDirectories = [*foundDirectories, *recursiveSearchOnPath(item_wholepath)]

        if search in item_wholepath:
            foundDirectories = [*foundDirectories, item_wholepath]

    return foundDirectories
    
def flattenSearchResults(pathList):
    all_files = []


if __name__=="__main__":

    for parameter in sys.argv[1:]:
        if "path=" in parameter:
            path = parameter[parameter.index("=")+1:]
        elif "dir=" in parameter:
            directory = parameter[parameter.index("=")+1:]
        else:
            print("Unknown parameter: ", parameter)
    
    results = recursiveSearchOnPath(path=path, search=directory)
    #print(results)
    
    [print(result) for result in results] if type(results) is not str else print(results)