# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        current = head
        lengthOfList = 1
        while current.next is not None:
            current = current.next
            lengthOfList += 1
        end = k % lengthOfList
        k = lengthOfList - end # main logic is this to find the how much rotation is required
        print(k)
        current.next = head
        while k>0:
            current = current.next
            k -= 1
        head = current.next
        current.next = None

        return head
        