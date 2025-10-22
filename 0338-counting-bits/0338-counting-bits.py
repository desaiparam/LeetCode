class Solution:
    def countBits(self, n: int) -> List[int]:
        #TC O(N log n) and SC O(1) now for the follow up
        # ans = [0]* (n+1)
        # for i in range(n+1):
        #     ans[i] = bin(i).count('1')
        # return ans
        # TC O(N) and no built in use
        ans = [0]* (n+1)
        for i in range(1,n+1):
            ans[i] = ans[i >> 1] + (i & 1) 
        return ans
        