import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        counter = 0
        for i in lists:
            if i:
                heapq.heappush(minheap,(i.val,counter,i))
                counter+= 1
        dummy = ListNode(0)
        curr = dummy
        while minheap:
            minval,_,minnode = heapq.heappop(minheap)
            curr.next = minnode
            curr = curr.next
            if minnode.next:
                heapq.heappush(minheap,(minnode.next.val,counter,minnode.next))
                counter += 1
        return dummy.next
        