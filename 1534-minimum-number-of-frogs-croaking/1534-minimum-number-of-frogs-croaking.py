class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        order = {'c':0,'r':1,'o':2,'a':3,'k':4}
        active = 0
        max_active = 0
        count = [0] * 5
        for i in croakOfFrogs:
            idx = order[i]
            if idx == 0:
                active += 1
                count[0] += 1
                max_active = max(max_active,active)
            else:
                if  count[idx-1] == 0:
                    return -1
                count[idx - 1] -= 1
                count[idx] += 1
            if idx == 4:
                active -=1
                count[4] -= 1
        if any(count):
            return -1
        return max_active
        