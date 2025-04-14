class Stack:
    def __init__(self):
        self.list=[]
    
    def push(self,item):
        self.list.append(item)
    
    def pop(self): # 꺼낸 값으로 처리를 하므로 return 시킴
        return self.list.pop() # pop(-1) : 최근에 넣은거 빠짐
    
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())