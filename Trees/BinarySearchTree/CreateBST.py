#  Binary Search Tree (BST):
# A Binary Search Tree (BST) is a special kind of binary tree where the values of the nodes are arranged in a specific order:
# The left child of a node contains values less than the node's value.
# The right child of a node contains values greater than the node's value.
# This ordering rule ensures that for any given node, its left subtree contains values less than the node, and its right subtree contains values greater than the node.
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def Insert(root,val):
    if not root:
        return Node(val)
    if(val<root.val):
        root.left=Insert(root.left,val)
    else:
        root.right=Insert(root.right,val)
    return root
def BuildBST(vals):
    root=None
    for val in vals:
        root=Insert(root,val)
    return root
#Searching in a BST
def Search(root,val):
    while(root!=None and root.val!=val):
        root= root.left if val<root.val else root.right
    return root
# Example input list
vals = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst_root = BuildBST(vals)
print(Search(bst_root,9))