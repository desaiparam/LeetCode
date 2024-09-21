class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        sets = defaultdict(int)
        ans = []
        for i in digits:
            sets[i] += 1
        for i in range(100, 999, 2):
            check = defaultdict(int)
            for d in str(i):
                check[int(d)] += 1
            if all(map(lambda x: x in sets and check[x] <= sets[x], check)):
                ans.append(i)
            # if indx % 2 == 0:
            # print(digit)
        return ans