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
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)
def InsertVal(root,val):
    if not root:
        return Node(val)
    curr=root
    while(True):
        if(val<curr.val):
            if(curr.left!=None):
                curr=curr.left
            else:
                curr.left=Node(val)
                break
        else:
            if(curr.right!=None):
                curr=curr.right
            else:
                curr.right=Node(val)
                break
    return root
vals = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst_root = BuildBST(vals)
inorder(bst_root)
print()
bst_root=InsertVal(bst_root,99)
inorder(bst_root)