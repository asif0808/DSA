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
def isSame(r,t):
    if not r and not t:
        return True
    if not r or not t:
        return False
    return (r.val==t.val) and isSame(r.left,t.left) and isSame(r.right,t.right)
def IssubTree(root,subroot):
    if not root:
        return False
    if isSame(root,subroot):
        return True
    return IssubTree(root.left,subroot) or IssubTree(root.right,subroot)
idx=-1
root=BuildBin([3, 4, 1, -1, -1, 2, -1, -1, 5, -1, -1])
idx=-1
subroot=BuildBin([4, 1, -1, -1, 3, -1, -1])
print(IssubTree(root,subroot))

