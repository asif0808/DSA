# In preorder traversal, the root node is processed first, followed by the left subtree, and finally the right subtree.
# The general traversal order is:
# Visit the root node.
# Traverse the left subtree (recursively).
# Traverse the right subtree (recursively).
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
#PreOrder Traversal
def PreOrder(root):
    if(root==None):
        return
    print(root.val)
    PreOrder(root.left)
    PreOrder(root.right)
idx=-1
root=BuildBin([1,2,-1,-1,3,4,-1,-1,5,-1,-1])            #-1 treated as None
PreOrder(root)