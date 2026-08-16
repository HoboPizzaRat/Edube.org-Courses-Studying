class QueueError(Exception):
    
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

class Queue:
    def __init__(self):
        self.__queue = []
        self.__size = 0

    def isempty(self):
        return self.__size == 0

    def put(self, item):
        self.__queue.append(item)
        self.__size += 1

    def get(self):
        if not self.isempty():
            val = self.__queue[0]
            self.__queue[:1]
            self.__size -= 1
            return val
        else:
            return None
        
class SuperQueue(Queue):
    
    def __init__(self):
        self.__err = QueueError("Cannot get item from empty queue", 400)
        Queue.__init__(self)

    def put(self, item):
        Queue.put(self, item)
    
    def get(self):
        item = Queue.get(self)
        if item == None:
            raise self.__err 
        return item


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

# purposefully created queue error
que.get()
# remove the above line for errorless execution