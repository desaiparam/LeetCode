class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        print(sorted_s)
        print(sorted_t)
        return sorted_s == sorted_t