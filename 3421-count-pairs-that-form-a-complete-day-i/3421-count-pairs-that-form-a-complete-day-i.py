from collections import defaultdict
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
       #SOULUTION 1
        # c = 0
        # for i in range(len(hours)):
        #     for j in range(i+1,len(hours)):
        #         if (hours[i] + hours[j] )% 24 == 0:
        #             c +=1
        #     # elif hours[i] % 24 == 0:
        #     #     print(hours[i])
        #     #     c += 1
       
        # return c 

        #SOLUTION 2 
        remainder_c = defaultdict(int)
        c = 0
        for i in hours:
            if i % 24 == 0:
                c += remainder_c[0]
            else:
                c += remainder_c[24 - (i % 24)]
            remainder_c[(i % 24)] += 1
        return c


        