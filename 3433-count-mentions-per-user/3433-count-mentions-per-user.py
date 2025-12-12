class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[-1]))
        # print(events)
        ans = [0] * numberOfUsers
        online = [True] * numberOfUsers
        minheap = []
        for e,t,i in events:
            # print(ans,online,minheap)
            while minheap and minheap[0][0] <= int(t):
                    mintime, user = heapq.heappop(minheap)
                    online[user] = True
            if e == "MESSAGE":  
                parts = i.split()
                if i == "ALL":
                    for c in range(numberOfUsers):
                        ans[c] += 1
                elif i == "HERE":
                    for c in range(numberOfUsers):
                        if online[c]:
                            ans[c] += 1
                else:
                    for p in parts:
                        user = int(p[2:])
                        # if online[user]: 
                        ans[user] += 1
            elif e == "OFFLINE":
                online[int(i)] = False
                heapq.heappush(minheap,(int(t)+60,int(i)))
        return ans
