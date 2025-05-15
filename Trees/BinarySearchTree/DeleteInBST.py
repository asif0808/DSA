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
def DeleteNode(root,key):
    if not root:
        return root
    if key<root.val:
        root.left=DeleteNode(root.left,key)
    elif key>root.val:
        root.right=DeleteNode(root.right,key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        #find minimum of right subtree
        cur=root.right
        while cur.left:
            cur=cur.left
        root.val=cur.val
        rooot.right=DeleteNode(root.right,root.val)
    return root
vals = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst_root = BuildBST(vals)
inorder(bst_root)
print()
bst_root=DeleteNode(bst_root,13)
inorder(bst_root)