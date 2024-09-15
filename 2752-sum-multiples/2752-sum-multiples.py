class Solution:
    def sumOfMultiples(self, n: int) -> int:
        
        # for i in range(1,n+1):
        #     if i%3 == 0:
        #         sum+=i
        #         print("i 3",i)
        #         print("sum 3",sum)
        #     elif i%5 == 0:
        #         sum+=i
        #         print("i 5",i)
        #         print("sum 5",sum)
        #     elif i%7 == 0:
        #         sum +=i
        #         print("i 7",i)
        #         print("sum 7",sum)
        return sum([i for i in range(1,n+1) if i % 3 ==0 or i % 5 ==0 or i % 7 ==0 ])