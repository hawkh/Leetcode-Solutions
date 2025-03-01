# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1=[]
        leaf2=[]
        def getleaf(root,res):
            if root.left is None and root.right is None:
                res.append(root.val)
                return 
            if root.left:
                getleaf(root.left,res)
            if root.right:
                getleaf(root.right,res)
            return 
        getleaf(root1,leaf1)
        getleaf(root2,leaf2)
        return leaf1==leaf2
        