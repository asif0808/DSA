# Inorder Traversal (BST or General Binary Tree):
# In inorder traversal, the left subtree is processed first, followed by the root node, and finally the right subtree.
# The general traversal order is:
# Traverse the left subtree (recursively).
# Visit the root node.
# Traverse the right subtree (recursively).
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
#InOrder Traversal
def InOrder(root):
    if(root==None):
        return
    InOrder(root.left)
    print(root.val)
    InOrder(root.right)
idx=-1
root=BuildBin([1,2,-1,-1,3,4,-1,-1,5,-1,-1])            #-1 treated as None
InOrder(root)