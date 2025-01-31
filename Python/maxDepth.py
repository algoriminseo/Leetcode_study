# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity : O(n), where n is number of nodes
# Space complexity : O(h). where h is depth of the tree
# It could be the skewed tree to calculate length.

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 
        if not root.left and not root.right:
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 