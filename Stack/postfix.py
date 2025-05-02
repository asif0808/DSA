#postfix or reverse polish notation
class Rpn:
    def __init__(self):
        self.stack=[]
    def postfix(self,s):
        for i in s:
            if i=='+':
                new=self.stack.pop()+self.stack.pop()
                self.stack.append(new)
            elif i=='-':
                a,b=self.stack.pop(),self.stack.pop()
                self.stack.append(b-a)
            elif i=='*':
                new=self.stack.pop()*self.stack.pop()
                self.stack.append(new)
            elif i=='/':
                a,b=self.stack.pop(),self.stack.pop()
                self.stack.append(int(b/a))          #in python 2 self.stack.append(int(float(b)/a))
            else:
                self.stack.append(int(i))
        return self.stack[0]
obj=Rpn()
print(obj.postfix(["2","1","+","3","*"]))
