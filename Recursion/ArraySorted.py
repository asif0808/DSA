#check if array is sorted or not using recursion
def IsSorted(arr,n):
    if(n==0 or n==1):
        return True
    return arr[n-1]>arr[n-2] and IsSorted(arr,n-1)

print(IsSorted([2,3,4,6,5,4],6))