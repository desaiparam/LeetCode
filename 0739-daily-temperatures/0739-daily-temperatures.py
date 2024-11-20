class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        que = deque()
        for i in range(len(temperatures)-1,-1,-1):
            que.append((temperatures[i],0))
        ans = []
        # print(que)
        for idx , (value,lt) in enumerate(que):
            while stack and stack[-1][0] <= value:
                stack.pop()
            if stack:
                lt = idx - stack[-1][-1]
            else:
                lt = 0
            stack.append((value,idx))
            ans.append(lt)
        return ans[::-1]
