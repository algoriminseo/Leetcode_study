# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#           
#
# Time complexity : O(n), where n is number of nodes. Have to iterate through all nodes in the tree
# Space complexity : O(h), where h is height of the tree. Due to recurison stack, everytime, we have to return the nodes. 
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)