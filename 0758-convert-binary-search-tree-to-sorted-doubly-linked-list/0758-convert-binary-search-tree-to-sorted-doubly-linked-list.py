"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.head = None
        self.prev = None
        def helper(root):
            if not root:
                return None
            
            helper(root.left)
            if self.prev:
                self.prev.right = root
                root.left = self.prev
            else:
                self.head = root
            self.prev = root
            helper(root.right)
        helper(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
        
        