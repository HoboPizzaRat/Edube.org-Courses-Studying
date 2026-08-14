blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
blocks_available = blocks
height = 0
while(blocks_available - height+1 >= 0):
    height += 1
    blocks_available -= height
    

print("The height of the pyramid:", height)
