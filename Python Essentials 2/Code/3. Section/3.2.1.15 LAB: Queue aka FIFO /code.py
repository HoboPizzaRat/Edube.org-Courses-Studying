class QueueError(): 
    pass
    
            


class Queue:
    def __init__(self):
        self.__queue = []


    def put(self, elem):
        self.__queue.append(elem)


    def get(self):
        if len(self.__queue) == 0:
            raise QueueError
        else:
            val = self.__queue[0]
            self.__queue = self.__queue[1:]
            return val


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
