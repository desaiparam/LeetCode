"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode
        current = head
        while current.next != head:
            if current.val <= insertVal <= current.next.val:
                break
            # if current.val <= insertVal and current.next == head:
            #     break
            if current.val > current.next.val and (current.val <= insertVal or insertVal <= current.next.val):
                break
            # if current.val >= insertVal and current.next == head: #this was for case [1,0] and all such cases
            #     break
            current = current.next
        # print(current.val)
        newNode.next = current.next
        current.next = newNode
        return head