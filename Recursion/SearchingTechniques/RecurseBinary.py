def RecBin(a,start,end,target):
    mid=(start+end)//2
    if(start<=end):    
        if(a[mid]==target):
            return mid
        elif(a[mid]<target):
            return RecBin(a,mid+1,end,target)
        else:
            return RecBin(a,start,mid-1,target)
    return -1
a=[2,3,4,5,6,7]
n=len(a)
print(RecBin(a,0,n,6))