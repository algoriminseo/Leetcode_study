# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity : O(n), where n is number of nodes. when the tree is skewed to left or right,
# we can see that the method will go all the way to leaf node
# Space complexity : O(h) where h is height of the tree. 
# If tree is skewed, the node will be added because of the recurision stack
#Our memory complexity is determined by the number of return statements because each function call will be stored on the program stack. 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.height(root)!= -1)

    def height(self, root):
        if not root:
            return 0
        left, right = self.height(root.left), self.height(root.right)
        if left < 0 or right < 0:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
        