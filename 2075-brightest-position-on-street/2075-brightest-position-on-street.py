class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        d = defaultdict(int)
        for i , dis in lights:
            d[i-dis] += 1
            d[i+dis+1] -= 1
        curr = 0
        max_id = -1
        max_val = float('-inf')
        
        for i ,j in sorted(d.items()):
            curr += j
            if curr > max_val:
                max_val , max_id = curr , i
        return max_id

        