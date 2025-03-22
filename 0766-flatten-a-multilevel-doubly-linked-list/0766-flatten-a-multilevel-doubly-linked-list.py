"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        child = []
        while current:
            if current.child:
                if current.next:
                    child.append(current.next)
                current.next = current.child
                current.next.prev = current
                current.child = None
            print(child)
            if not current.next and child:
                current.next = child.pop()
                current.next.prev = current
            current = current.next
        return head
        
        
        

        