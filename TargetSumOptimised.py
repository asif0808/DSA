#optimised way for getting the index of elements whose sum equals to target (Time Complexity- O(n))
a=[2,7,11,-15]
def Target():
    i=0
    result=list()
    target=-8
    j=len(a)-1
    while(i<j):
        ps=a[i]+a[j]
        if(ps<target):
            i+=1
        if(ps>target):
            j-=1
        if(ps==target):
            result.append(i)
            result.append(j)
            return result
print(Target())


