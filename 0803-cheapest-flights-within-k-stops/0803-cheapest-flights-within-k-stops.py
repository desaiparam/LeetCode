class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,price in flights:
            adj[u].append((v,price))
        heap = [(0,src,0)]
        best = {}
        while heap:
            cost,u,stops = heapq.heappop(heap)
            if u == dst:
                return cost
            if stops > k:
                continue
            for i,j in adj[u]:
                new_cost = cost + j
                stat = (i,stops-1)
                if stat not in best or new_cost < best[stat]:
                    best[stat] = new_cost
                    heapq.heappush(heap,(new_cost,i,stops+1))
        return -1



        
        