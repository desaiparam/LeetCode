class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # subString = []
        Count = 0
        for i in range(len(s)):
            subString=(s[i:i+3])
            if len(set(subString))==3:
                Count+=1
        return Count