class Leaderboard:

    def __init__(self):
        self.hashmap = defaultdict(int)
    def addScore(self, playerId: int, score: int) -> None:
        self.hashmap[playerId] += score

    def top(self, K: int) -> int:
        minheap = []
        for p,s in self.hashmap.items():
            heapq.heappush(minheap,-s)
        total = 0
        for i in range(K):
            total += -(heapq.heappop(minheap))
        return total

    def reset(self, playerId: int) -> None:
        del self.hashmap[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)