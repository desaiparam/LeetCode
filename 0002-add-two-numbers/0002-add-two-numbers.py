# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        curr1 = l1
        curr2 = l2
        total = 0
        carry = 0
        while curr1 or curr2 or carry:
            total = carry
            if curr1:
                total += curr1.val
                curr1 = curr1.next
            if curr2:
                total += curr2.val
                curr2 = curr2.next
            carry = total // 10
            dummy.next= ListNode(total%10)
            dummy = dummy.next
        return res.next

            

        