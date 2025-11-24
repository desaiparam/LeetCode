"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapy = {}
        q = deque([node])
        def clone(node):
            if not node:
                return None
            if node in mapy:
                return mapy[node]
            mapy[node] = Node(node.val)
            return mapy[node]
        while q:
            curr = q.popleft()
            copy = clone(curr)
            for n in curr.neighbors:
                if n not in mapy:
                    q.append(n)
                copy.neighbors.append(clone(n))
        return mapy[node]
