#kadane's alogrithm provides most optimised way to get max subarray sum
a=[3,-4,5,4,-1,7,-8]
maxsum=float('-inf')
cursum=0
for i in range(len(a)):
    cursum+=a[i]
    maxsum=max(cursum,maxsum)
    if(cursum<0):
        cursum=0
print(maxsum)