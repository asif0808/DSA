# ✅ Level Order Traversal (Breadth-First Search - BFS)
# Level order traversal means visiting the nodes of the binary tree level by level, from top to bottom and left to right at each level.

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
from collections import deque
def Levelorder(root):
    if not root:
        return []
    queue=deque([root])
    result=[]
    while queue:
        node=queue.popleft()
        result.append(node.val)
        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)
    return result
    
idx=-1
root=BuildBin([1,2,-1,-1,3,4,-1,-1,5,-1,-1])            #-1 treated as None
print(Levelorder(root))