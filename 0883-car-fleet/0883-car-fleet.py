class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(speed)):
            pairs.append([position[i],speed[i]])
        pairs = sorted(pairs)[::-1]
        # pairs.sort()
        print(pairs)
        for i,j in pairs:
            time = (target - i)/j
            # print(time)
            stack.append(time)
            # print(stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)