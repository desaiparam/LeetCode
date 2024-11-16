# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        sub = {}
        ans = []

        def s(node):
            if not node:
                return ''
            left = s(node.left)
            right = s(node.right)
            subt = f'{node.val},{left},{right}'
            # print("subt",subt)
            sub[subt] = sub.get(subt,0)+1
            # print("sub",sub)
            if sub[subt] == 2:
                # print(sub[subt])
                ans.append(node)
            return subt
        s(root)
        # self._in_order_traversal(root)
        return ans

    # def _in_order_traversal(self, node: Optional[TreeNode]):
    #     if node is None:
    #         return
    #     # Traverse the left subtree
    #     self._in_order_traversal(node.left)
    #     # Print the current node's value
    #     self._in_order_traversal(node.right)
    #     print(node.val)
    #     # Traverse the right subtree