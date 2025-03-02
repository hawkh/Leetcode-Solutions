# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pathsums=defaultdict(int)
        self.paths=0
        self.pathsums[0]=1
        def dfs(r,currsum):
            if r is None:
                return 
            currsum+=r.val
            self.paths+=self.pathsums[currsum-targetSum]
            self.pathsums[currsum]+=1
            if r.right:
                dfs(r.right,currsum)
            if r.left:
                dfs(r.left,currsum)
            self.pathsums[currsum]-=1
        dfs(root,0)
        return self.paths
        