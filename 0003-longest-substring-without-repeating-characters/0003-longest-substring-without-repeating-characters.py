class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        maxy = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                left = max(left,hashmap[s[i]] + 1)
            hashmap[s[i]] = i
            maxy = max(maxy, i - left + 1)
        return maxy