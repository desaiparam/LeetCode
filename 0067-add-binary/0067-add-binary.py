class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carr = 0
        i = len(a) - 1
        j = len(b) - 1
        ans = []
        while i >= 0 or j >= 0 or carr:
            if i >= 0:
                carr += int(a[i])
                i -= 1
            if j >= 0:
                carr += int(b[j])
                j -= 1
            ans.append(str(carr %2 ))
            carr //=2

        return  ''.join(reversed(ans))
        