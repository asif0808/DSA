class MinStack:
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self,val):
        self.stack.append(val)
        if self.minStack:
            val=min(self.minStack[-1],val)
        self.minStack.append(val)
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minStack[-1]
    def show(self):
        return self.stack,self.minStack
obj=MinStack()
obj.push(5)
obj.push(3)
obj.push(4)
obj.push(10)
print(obj.show())