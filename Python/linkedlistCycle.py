# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Using two pointers
#Time complexity : O(n), where n is number of nodes. 
# Need to iterate through whole nodes for comparing those values
#Space complexity : O(1), Does not need to store anything

#Using set
#Time Complexity : O(n), where n is number of nodes
#SAME reason
#Space complexity : O(n), where n is number of nodes
#Have to allocate extra memory space to store elements in the set
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        myset = []
        myset = set(myset)
        if head == None or head.next == None:
            return False
        return self.check_Dup(head, myset)
    def check_Dup(self, head, myset):
        if head.next == None:
            return False
        if head in myset:
            return True
        else:
            myset.add(head)
            return self.check_Dup(head.next,myset )
       
        # mymap = set()
        # curr_node = head

        # while curr_node:
        #     if curr_node in mymap:
        #         return True
        #     mymap.add(curr_node)    
        #     curr_node = curr_node.next
        # return False


        # slow = head
        # fast = head


        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow.val == fast.val:
        #         return True
        # return False

            
        
