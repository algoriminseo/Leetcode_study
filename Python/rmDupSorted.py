
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Time complexity : O(n),  where n is number of nodes. Since we remove duplicates in the 
#array, in the worst case scenario, it will search for whole nodes.
#Space complexity : O(1), No need for extra space
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = head
        while head and head.next:
            if head.value == head.next.value:
                head.next = head.next.next
            else:
                head = head.next
        return ans
    
