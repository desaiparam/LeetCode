class Solution:
    def climbStairs(self, n: int) -> int:
        pr1=1
        pr2=0
        for i in range(1,n+1):
            curi =pr1+pr2
            print("curi",curi)
            pr2=pr1
            print("pr2",pr2)
            print("pr1",pr1)
            pr1 = curi
        return pr1        

                

            
        