# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=[root]
        nextq=[]
        level=[]
        res=[]
        while(q!=[]):
            for root in q:
                level.append(root.val)
                if root.left is not None:
                    nextq.append(root.left)
                if root.right is not None:
                    nextq.append(root.right)
            res.append(level)
            level=[]
            q=nextq
            nextq=[]
        return res

        