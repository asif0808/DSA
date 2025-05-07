def binSearch(arr,srch):
    first=0
    last=len(arr)-1
    while first<=last:
        mid=(first+last)//2
        if(srch==arr[mid]):
            return mid
        elif(srch<arr[mid]):
            last=mid-1
        else:
            first=mid+1
    return 'not found'
print(binSearch([2,3,4,5],6))
