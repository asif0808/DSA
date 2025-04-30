#bruteforce approach
#finding subarray with maximum sum
a=[3,-4,5,4,-1,7,-8]
#test cases 
#a=[-4,-5,-3,-9,-8,0,-1]
#a=[0,0,0,-2,-4,1]
n=len(a)
start=0
end=0
maxsum=float('-inf')
for i in range(n):
    cursum=0
    for j in range(i,n):
        cursum+=a[j]
        maxsum=max(cursum,maxsum)
print(maxsum)
