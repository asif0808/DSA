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
def SymmetricTree(root):
    def mirror(r1,r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return (r1.val==r2.val) and mirror(r1.left,r2.right) and mirror(r1.right,r2.left)
    return mirror(root,root)
idx=-1
root=BuildBin([1,
 2, 3, -1, -1, 4, -1, -1,
 2, 4, -1, -1, 3, -1, -1]
)   
print(SymmetricTree(root))

