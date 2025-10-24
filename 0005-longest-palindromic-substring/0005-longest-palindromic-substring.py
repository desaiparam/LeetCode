class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxy = 0
        result = ""
        for i in range(n):
            j = i - 1
            k = i + 1
            while j >= 0 and k < n and s[j] == s[k]:
                if k - j + 1 > maxy:
                    maxy = k - j + 1
                    result = s[j:k+1]
                j -= 1
                k += 1
            j = i
            k = i + 1
            while j >= 0 and k < n and s[j] == s[k]:
                if k - j + 1 > maxy:
                    maxy = k - j + 1
                    result = s[j:k+1]
                j -= 1
                k += 1
        return result or s[0]
        