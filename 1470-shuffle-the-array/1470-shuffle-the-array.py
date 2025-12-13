class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        i = 0
        while i < n:
            output.append(nums[i])
            output.append(nums[i+n])
            i += 1
        return output