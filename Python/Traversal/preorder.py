# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity : O(n), where n is number of nodes. We need to search all nodes in the tree
# Space complexity : O(n), where n is number of nodes. We need to put all nodes in the list.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(root):
            if not root:
                return []
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
            return ans
        
        return preorder(root)
