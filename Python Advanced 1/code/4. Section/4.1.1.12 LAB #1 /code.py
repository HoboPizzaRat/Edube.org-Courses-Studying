# 0. Your task is to write a code that will prepare a proposal of 
# reduced prices for the candies whose total weight exceeds 300 units 
# of weight (we don’t care whether those are kilograms or pounds)
# 1. Your input is a list of dictionaries; each dictionary represents one 
# type of candy. Each type of candy contains a key entitled 'weight', 
# which should lead you to the total weight details of the given delicacy. 
# The input is presented in the editor;
# 2. Prepare a copy of the source list (this should be done with a one-liner) 
# and then iterate over it to reduce the price of each delicacy by 20% if 
# its weight exceeds the value of 300;
# 3. Present an original list of candies and a list that contains 
# the proposals;
# 4. Check if your code works correctly when copying and modifying 
# the candy item details.
import copy

warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print('Source list of candies')
for item in warehouse:
    print(item)

warehouse2 = copy.deepcopy(warehouse)
for item in warehouse2:
    if item["weight"] > 500:
        item["price"] = item["price"]*0.80
print("******************")
print("Price Proposal")
for item in warehouse2:
    print(item)