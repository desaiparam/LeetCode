class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        # seq = []
        for i in zip(*strs):
            if list(i) != sorted(i):   
                count += 1
        return count

        