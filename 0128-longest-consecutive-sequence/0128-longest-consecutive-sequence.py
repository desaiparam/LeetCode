class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        # print(hashmap)
        counter = 0
        for i in hashmap:
           if i - 1 not in hashmap:
                length = 1
                while length + i in hashmap:
                    # print(i+length)
                    length += 1
                counter = max(counter,length)
        
        return counter
                
        