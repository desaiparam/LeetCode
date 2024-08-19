# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if slow is None or head.next is None:
            return False
        fast = head.next
        while fast and fast.next:
            # slow=head.next
            # fast=head.next
            # print("slow:", slow.val if slow else None)
            # print("fast:", fast.val if fast else None)
            if fast == slow :
                return True
            slow=slow.next
            fast=fast.next.next
            # else:

                # return False
        return False
        