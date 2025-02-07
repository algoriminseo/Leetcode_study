# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time Complexity : O(nlogn) where n is number of nodes. The worst case, we need to create n lists due to creating sublists , and due to tree recursion, it is log n.
#Space Complexity :  O(nlogn), where n is number of nodes. Have to create new array, and new space for trees
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        
        if length == 0:
            return None
        
        mid = length // 2
        
        root = TreeNode(nums[mid])
        root.right = self.sortedArrayToBST(nums[mid+1 :])
        root.left = self.sortedArrayToBST(nums[ :mid])
        return root
