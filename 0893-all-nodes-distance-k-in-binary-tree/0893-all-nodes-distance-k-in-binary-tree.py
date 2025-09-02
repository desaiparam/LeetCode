# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def markParent(root):
            q = deque([root])
            while q:
                curr = q.popleft()
                if curr.left:
                    parent[curr.left] = curr
                    q.append(curr.left)
                if curr.right:
                    parent[curr.right] = curr
                    q.append(curr.right)
        markParent(root)
        q = deque([target])

        print(parent)
        visited = set()
        visited.add(target)
        currLevel = 0
        while q:
            if currLevel == k:
                return [root.val for root in q]
            currLevel += 1      
            for _ in range(len(q)):     
                curr = q.popleft()        
                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited.add(curr.left)
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited.add(curr.right)
                if parent.get(curr) and parent.get(curr) not in visited:
                    q.append(parent[curr])
                    visited.add(parent[curr])
        return []








        