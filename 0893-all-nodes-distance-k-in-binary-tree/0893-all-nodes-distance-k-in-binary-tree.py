# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        trackParent = {}
        def markParents(root,trackParent):
            q = deque([root])
            while q:
                curr = q.popleft()
                if curr.left:
                    trackParent[curr.left] = curr
                    q.append(curr.left)
                if curr.right:
                    trackParent[curr.right] = curr
                    q.append(curr.right)
        markParents(root,trackParent)
        visited = set()
        q = deque([target])
        visited.add(target)
        curr_level = 0
        while q:
            if curr_level == k:
                return [root.val for root in q]
            curr_level += 1
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited.add(curr.left)
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited.add(curr.right)
                if trackParent.get(curr) and trackParent.get(curr) not in visited:
                    q.append(trackParent[curr])
                    visited.add(trackParent[curr])
        return []

                
        