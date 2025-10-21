class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #    using KMP algo
        n = len(needle)
        lps = [0] * n
        def preprocess(st):
            lps[0] = 0
            i = 1
            j = 0
            while i < n:
                if st[i] == st[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                elif st[i] != st[j] and j > 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        preprocess(needle)
        i = 0 
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if n == j:
                    return i - j
            elif haystack[i] != needle[j] and j > 0:
                j = lps[j-1]
            else:
                i += 1
        return -1





