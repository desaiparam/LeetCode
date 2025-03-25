# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Solution 1 
        # prev = None
        # curr = head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
            
        # return prev
        #SOLUTION 2 USING RECURSION
        if not head or not head.next:
            return head
        current = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return current