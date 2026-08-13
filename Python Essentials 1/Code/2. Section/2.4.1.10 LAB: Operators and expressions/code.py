def calculate(input, calc) :
    return calc(input)

func = lambda x: 3*x**3 - 2*x**2 + 3*x - 1

print("##########################")
x = 0
print("x =", x)
y = calculate(x, func)
print("y =", y)
print("##########################")
x = 1
print("x =", x)
y = calculate(x, func)
print("y =", y)
print("##########################")
x = -1
print("x =", x)
y = calculate(x, func)
print("y =", y)
print("##########################")
