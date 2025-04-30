#Brute-Force Approach (Time Complexity- O(n^2))
#return the pair of index/element of array whose sum is equal to given target
arr=[2,7,11,15]
target=13
pairIndex=list()
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==target):
            pairIndex.append(i)
            pairIndex.append(j)
print(pairIndex)