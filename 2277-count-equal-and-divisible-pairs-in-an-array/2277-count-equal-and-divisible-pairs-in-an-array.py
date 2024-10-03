class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # i=0
        # j = len(nums) -1
        c = 0
        # while j != 0 and i != len(nums)-1 and i != j:
        #     print(nums[i],nums[j])
        #     print("i,j",i,j)
        #     if nums[i] == nums[j] and i*j % k == 0 :
        #         c += 1
        #     i += 1
        #     j -= 1
            # i += 1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    if nums[i] == nums[j] and i * j %k == 0:
                        c += 1
        return c
        
        