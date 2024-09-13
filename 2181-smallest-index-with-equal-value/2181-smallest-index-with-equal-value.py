class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        smaller = min(nums)
        # print(smaller)
        for i in range(len(nums)):
            print("i",i)
            if(i%10==nums[i]):
                print("nums[i]",nums[i])
                if(smaller<nums[i]):
                    print("smaller",smaller)
                    return i
                else:
                    return i
        
        return -1