
#Review linked lsit https://www.youtube.com/watch?v=GfRQvf7MB3k
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Time complexity: O(m +n) where m is length of list1, n is length of list2. It depends of size of the array.
#Space complexity: O(1) Constant space (Not creating array)
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1 is not None:
            temp.next = list1
        
        elif list2 is not None:
            temp.next = list2
        
        return dummy.next
    


