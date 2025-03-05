class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # print(sorted_s)
        # print(sorted_t)
        # return sorted_s == sorted_t
        if len(s) != len(t):
            return False
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for i in t:
            count[i] -= 1
        for val in count.values():
            if val != 0:
                return False
        return True