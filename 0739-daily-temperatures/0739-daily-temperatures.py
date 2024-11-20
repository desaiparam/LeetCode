class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # que = deque()
        # for i in range(len(temperatures)-1,-1,-1):
        #     que.append((temperatures[i],0))
        # ans = []
        # # print(que)
        # for idx , (value,lt) in enumerate(que):
        #     while stack and stack[-1][0] <= value:
        #         stack.pop()
        #     if stack:
        #         lt = idx - stack[-1][-1]
        #     else:
        #         lt = 0
        #     stack.append((value,idx))
        #     ans.append(lt)
        # return ans[::-1]
        # stack = []
        # que = deque()
        ans = [0] * len(temperatures)
        heigh = 0
        print(heigh)
        for i in range(len(temperatures)-1,-1,-1):
            if heigh <= temperatures[i]:
                # ans.append()
                heigh = temperatures[i]
                continue
            day = 1
            while temperatures[day + i] <= temperatures[i]:
                day += ans[day + i]
            ans[i] = day
        return ans
