my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
uniques = []

for item in my_list:
    if item not in uniques:
        uniques.append(item)
    else:
        continue
    
    
print("The list with unique elements only:")
print(uniques)
