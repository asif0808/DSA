#OPtimised way to get max diameter of a binary tree (Time Complexity => O(n))
#Creating a binary tree
class Node():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def BuildBin(vals):
    global idx
    idx+=1
    #print(idx,id(idx))
    if(vals[idx]==-1):
        return None
    root=Node(vals[idx])
    root.left=BuildBin(vals)
    root.right=BuildBin(vals)
    return root
def MaxDiameter(root):
    ans=[0]
    def height(root):
        if(root==None):
            return 0
        left_h=height(root.left)
        right_h=height(root.right)
        ans[0]=max(left_h+right_h,ans[0])
        return max(left_h,right_h)+1
    height(root)
    return ans[0]
idx=-1
root=BuildBin([1,2,-1,-1,3,4,-1,-1,5,-1,-1])  
print(MaxDiameter(root))
