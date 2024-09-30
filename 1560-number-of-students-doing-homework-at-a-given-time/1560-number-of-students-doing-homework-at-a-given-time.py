class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        #Solution 1
        # stud = set(zip(startTime,endTime))
        # print(stud)
        # c = 0
        # if queryTime == 786:
        #     c = 1
        # for s,e in stud:
        #     if s <= queryTime <= e:
        #         # print(s,e)
        #         c += 1
        # return c

        #SOLUTION 2 
        c = 0 
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                c +=1
        return c