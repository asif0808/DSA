#create binary tree
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
def SameTree(r1,r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    return (r1.val==r2.val) and SameTree(r1.left,r2.left) and SameTree(r1.right,r2.right)
idx=-1
root1=BuildBin([1,
 2, 3, -1, -1, 4, -1, -1,
 2, 4, -1, -1, 3, -1, -1]
)   
idx=-1
root2=BuildBin([1,
 2, 3, -1, -1, 4, -1, -1,
 2, 4, -1, -1, 3, -1, -1]
)   
print(SameTree(root1,root2))

