#printing all subsets using recursion and backtracking
def PrintSubset(arr,ans,i):
    if(i==len(arr)):
        print(ans)
        return
    ans.append(arr[i])
    PrintSubset(arr,ans,i+1)
    ans.pop()
    PrintSubset(arr,ans,i+1)
ans=[]
PrintSubset([1,2,2,3],ans,0)