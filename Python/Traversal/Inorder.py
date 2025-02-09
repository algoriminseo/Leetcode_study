# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity : O(n), where n is number of nodes. We need to search all nodes in the tree
# Space complexity : O(n), where n is number of nodes. We need to put all nodes in the list.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        stack = []

        while res or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            res.append(root)
            root = root.right
        return res               
            