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
def Min(root):
    if not root:
        return None
    cur=root
    while cur.left:
        cur=cur.left
    print(cur.val)
def Max(root):
    if not root:
        return None
    cur=root
    while cur.right:
        cur=cur.right
    print(cur.val)
vals = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst_root = BuildBST(vals)
inorder(bst_root)
print()
Min(bst_root)
Max(bst_root)