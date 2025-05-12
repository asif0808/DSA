#Time Complexity => O(n^2)
#creating a binary tree
class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def BuildBin(vals):
    global idx
    idx+=1
    if(vals[idx]==-1):
        return None
    root=Node(vals[idx])
    root.left=BuildBin(vals)
    root.right=BuildBin(vals)
    return root
def maxdepth(root):
    if(root==None):
        return 0
    left_depth=maxdepth(root.left)
    right_depth=maxdepth(root.right)
    return max(left_depth,right_depth)+1
def MaxDiameter(root):
    if (root==None):
        return 0
    left_d=MaxDiameter(root.left)
    right_d=MaxDiameter(root.right)
    curr_d=maxdepth(root.left)+maxdepth(root.right)
    return max(left_d,right_d,curr_d)
idx=-1
root=BuildBin([1,2,-1,-1,3,4,-1,-1,5,-1,-1])   
print(MaxDiameter(root))