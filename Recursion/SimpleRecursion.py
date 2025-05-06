def printNums(n):
    if(n==0):              #or if(n==1): print(n) return
        return 
    print(n,end=" ")
    printNums(n-1)
printNums(100)

