# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time complexity: O(n), where n is length of the input It traversals for all nodes.
#Space compleity: O(n), where n is length of inorder array. In the worst case when
# tree is balanced, we have to append all the nodes. 

#recursion
# class Solution(object):
    
#     def inorderTraversal(self, root):
#         inorder =[]
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         self.traverse(root, inorder)

    

#     def traverse(self, root, inorder):
#         if root is None:
#             return
#         self.traverse(root.left, inorder)
#         inorder.append(root.val) 
#         self.traverse(root.right, inorder)

#iterative
class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        stack = [] 
        node = root

        while True:
            if node:    
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                else:
                    node = stack.pop()
                    ans.append(node.val)    
                    node = node.right
        return ans


