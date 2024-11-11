class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sl1 = set(list1)
        sl2 = set(list2)
        print(sl1)
        print(sl2)
        s = list(sl1.intersection(sl2))
        print(s)
        n = len(s)
        c = [0] * n
        for i in range(n):
            w = s[i]
            a = list1.index(w)
            b = list2.index(w)
            c[i] += a+b
        mini = min(c)
        ans = []
        for i in range(n):
            w = s[i]
            if c[i] == mini:
                ans.append(w)
        return ans