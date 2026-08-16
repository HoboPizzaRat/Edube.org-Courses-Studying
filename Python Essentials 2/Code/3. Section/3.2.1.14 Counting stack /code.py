class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
    # Fill the constructor with appropriate actions.
        Stack.__init__(self)
        self.__count = 0

    def get_counter(self):
        return self.__count

    def push(self, val):
        # we dont actually need to count the pushed elements, only popped?
        # self.__count += 1
        Stack.push(self, val)
        
    def pop(self):
        val = Stack.pop(self)
        self.__count += 1
        return val
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
