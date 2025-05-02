class Check:
    def mydef(self,s):
        stack=[]
        for i in s:
            if(i=='('or i=='[' or i=='{'):
                stack.append(i)
            else:
                if(len(stack)==0):
                    return False
                if(stack[-1]=='(' and i==')' or stack[-1]=='{' and i=='}' or stack[-1]=='[' and i==']'):
                    stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False
myobj=Check()
print(myobj.mydef('}{'))