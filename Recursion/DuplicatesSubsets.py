#Some arrays may contain duplicates subsets, printing all original subsets
def Subsets(nums):
    nums.sort()
    res=[]
    subset=[]
    def dfs(i):
        if(i>=len(nums)):
            res.append(subset[:])
            return
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        idx=i+1
        while(idx<len(nums) and nums[idx]==nums[idx-1]):
            idx+=1
        dfs(idx)
    dfs(0)
    return res
print(Subsets([1,2,2,3]))