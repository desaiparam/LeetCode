# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        self.maxFreq = 0
        def helper(root):
            if not root:
                return 0
            leftSum = helper(root.left)
            rightSum = helper(root.right)
            subSum  =  leftSum + rightSum + root.val
            freq[subSum] = freq.get(subSum,0) + 1
            self.maxFreq = max(self.maxFreq,freq[subSum])
            return subSum
        helper(root)
        return [i for i,vals in freq.items() if vals == self.maxFreq]


