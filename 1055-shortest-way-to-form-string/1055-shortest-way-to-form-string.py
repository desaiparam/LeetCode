class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        mapy = defaultdict(list)
        for i,c in enumerate(source):
            mapy[c].append(i)
        def bs(lis,target):
            low = 0
            high = len(lis)-1
            while low <= high:
                mid = low + (high - low)//2
                if lis[mid] == target:
                    return mid
                elif lis[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        i = 0
        j = 0
        count = 0
        while j < len(target):
            tchar = target[j]
            if tchar not in mapy:
                return -1
            lis = mapy[tchar]
            idx = bs(lis,i)
            if idx == len(lis):
                i = lis[0]
                count += 1
            else:
                i = lis[idx]
                i += 1
                j += 1
                if j == len(target):
                    return count + 1
            if i == len(source):
                i = 0
                count += 1
        return -1
