class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {}
        miny = min(nums)
        maxy = max(nums)
        result = 0
        flag = False
        print(miny,maxy)
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for i in range(miny,maxy+1):
            if i not in hashmap:
                continue
            if flag:
                hashmap[i] -= 1
            freq = hashmap[i]
            if freq%2 == 0:
                result += (freq//2) * i
                flag = False
            else:
                result += (freq//2) * i
                result += i
                flag = True
        return result