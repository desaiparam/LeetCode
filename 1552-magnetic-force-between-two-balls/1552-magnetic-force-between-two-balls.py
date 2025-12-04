class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2:
            return position[-1] - position[0]

        def greedy(mid):
            count = 1
            last = position[0]
            for i in position:
                if  i - last >= mid:
                    last = i
                    count += 1
                    if count == m:
                        return True
            return False
        
        low = 0
        high = position[-1]
        ans = 1
        while low <= high:
            mid = low + (high - low) //2
            if greedy(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans 



        