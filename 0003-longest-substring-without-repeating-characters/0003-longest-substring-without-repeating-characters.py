class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs =0
        max_length=0
        sets={}
        for i in range(len(s)):
            if s[i] in sets:
                maxs=max(maxs,sets[s[i]]+1)
            sets[s[i]] = i
            max_length = max(max_length,i-maxs+1)
        return max_length 
        