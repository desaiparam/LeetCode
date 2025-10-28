class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hashmap = {}
        maxi = float('-inf')
        left = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                left = max(left,hashmap[s[i]]+1)
            hashmap[s[i]] = i
            maxi = max(maxi,i-left+1)
        return maxi
        