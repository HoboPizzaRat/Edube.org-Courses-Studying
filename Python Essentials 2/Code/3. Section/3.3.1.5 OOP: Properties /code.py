class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)

# As you can see, the class' __dict__ contains much more data 
# than its object's counterpart. Most of them are useless now - 
# the one we want you to check carefully shows the current varia value.