class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def count(i):
            p = int(i **(1/3))
            for j in (p-1,p,p+1):
                if j > 1 and j ** 3 == i and prime(j):
                    return 1 + j+j*j+i
            for p in range(2,int(i**0.5)+1):
                if i % p ==0:
                    q = i//p
                    if p != q and prime(p) and prime(q):
                        return 1 + p + q + i
                    break
            return 0

                            
        def prime(p):
            if p < 2:
                return False
            for i in range(2,int(p**0.5)+1):
                if p % i == 0:
                    return False
            return True
        ans = 0
        for i in nums:
            ans += count(i)
        return ans

