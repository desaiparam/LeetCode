# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        que = deque([root] if root else [])
        while que:
            level = []
            for i in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level = list(reversed(level)) if len(res) % 2 else level
            res.append(level)
        return res



        
        