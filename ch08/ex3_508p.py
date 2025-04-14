class Queue:
    def __init__(self):
        self.list=[]

    def enqueue(self,item): # 인큐
        self.list.append(item)
    
    def dequeue(self): # 디큐
        return self.list.pop(0) # pop(0) : 가장 오래된거 빠짐

queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())