class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        result = ""
        maxy = float('-inf')
        for i in range(n):
            k = i - 1
            j = i + 1
            while k >= 0 and j < n and s[j] == s[k]:
                if j - k + 1 > maxy:
                    maxy = j-k+1
                    result = s[k:j+1]
                j += 1
                k -= 1
            j = i +1
            k = i 
            while k >= 0 and j < n and s[j] == s[k]:
                if j - k + 1 > maxy:
                    maxy = j-k+1
                    result = s[k:j+1]
                j += 1
                k -= 1
        return result or s[0]