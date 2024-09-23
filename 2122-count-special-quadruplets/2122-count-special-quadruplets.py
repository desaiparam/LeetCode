class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        sets = defaultdict(int)
        for i in range(2,len(nums)):
            # print(nums[i:i+4])
            b = i-1
            # print(b)
            for j in range(b):
                sets[nums[j] + nums[b]] += 1
                print(nums[j] + nums[b])
            for j in range(i+1,len(nums)):
                count += sets[nums[j] - nums[i]] 
                print(count)
        return count
        