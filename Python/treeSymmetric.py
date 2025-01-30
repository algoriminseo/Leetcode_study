# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n), where n is number of nodes
    # Space Complexity: O(h), where h is height of tree
    # In the worst case scenario, the tree will be the left or right skewed tree 
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right :
            return True
        return self.helper( root.left, root.right)

    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left) 
        return False