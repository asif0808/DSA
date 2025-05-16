class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def BuildBST(nums):
    def Build(left,right):
        if left>right:
            return None
        mid=(left+right)//2
        root=Node(nums[mid])
        root.left=Build(left,mid-1)
        root.right=Build(mid+1,right)
        return root
    return Build(0,len(nums)-1)
def InOrdershow(root):
    if not root:
        return
    InOrdershow(root.left)
    print(root.val)
    InOrdershow(root.right)
root=BuildBST([1,2,3,4,5])
InOrdershow(root)