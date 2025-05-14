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
def IsBalanced(root):
    def check(root):
        if not root:
            return -1
        left_h=check(root.left)
        if left_h==-1:
            return -1
        right_h=check(root.right)
        if right_h==-1:
            return -1
        if abs(left_h-right_h)>1:
            return -1
        return 1+max(left_h,right_h)
    return check(root)!=-1
idx=-1
root=BuildBin([1,2,-1,3,-1,-1,-1])   
print(IsBalanced(root))

