x = float(input("Enter value for x: "))

# Write your code here.
def calculateTwat(x):
    result = x + 1/x
    result = x + 1/result
    result = x + 1/result
    result = 1/result

y = calculateTwat(x)
print("y =", y)

# results when input is 1
# expected: 0.6000000000000001
# gottten : 0.6000000000000001
# excellent