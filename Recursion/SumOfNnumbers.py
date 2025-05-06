def sum(nums):
    if(nums==1):
        return 1
    return nums+sum(nums-1)
print(sum(10))