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
def maxdepth(root):
    if(root==None):
        return 0
    left_depth=maxdepth(root.left)
    right_depth=maxdepth(root.right)
    return max(left_depth,right_depth)+1
idx=-1
root=BuildBin([1,2,-1,-1,3,4,-1,-1,5,-1,-1])  
print(maxdepth(root))