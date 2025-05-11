# Postorder Traversal (BST or General Binary Tree):
# In postorder traversal, the left subtree is processed first, followed by the right subtree, and finally the root node.
# The general traversal order is:
# Traverse the left subtree (recursively).
# Traverse the right subtree (recursively).
# Visit the root node.

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
def Postorder(root):
    if(root==None):
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.val)

idx=-1
root=BuildBin([1,2,-1,-1,3,4,-1,-1,5,-1,-1])            #-1 treated as None
Postorder(root)