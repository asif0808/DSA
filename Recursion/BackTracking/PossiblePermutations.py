def Total_Permutations(nums,idx,ans):
    if(idx==len(nums)):
        ans.append(nums[:])
        return
    for i in range(idx,len(nums)):
        nums[idx],nums[i]=nums[i],nums[idx]
        Total_Permutations(nums,idx+1,ans)
        nums[idx],nums[i]=nums[i],nums[idx]  #BackTracking
ans=[]
Total_Permutations([2,3,1],0,ans)
print(ans)