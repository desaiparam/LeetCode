class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hashmap = {}
        j = 0
        maxi = float('-inf')
        for i in range(len(s)):
            if s[i] in hashmap:
               j = max(hashmap[s[i]]+1,j)
            hashmap[s[i]] = i 
            maxi = max(maxi,i-j+1)
        return maxi
            
