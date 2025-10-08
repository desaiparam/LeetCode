import heapq     
class Tweet:
    def __init__(self,tId,time):
        self.tweetId = tId 
        self.timeStamp = time
class Twitter:
    def __init__(self):
        self.followeesMap = {}
        self.tweetsMap = {}
        self.time = 0        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetsMap:
            self.tweetsMap[userId] = []
        tweet = Tweet(tweetId,self.time)
        self.time += 1
        self.tweetsMap[userId].append(tweet)
        self.follow(userId,userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        follow = self.followeesMap.get(userId)
        if follow:
            for i in follow:
                tweets = self.tweetsMap.get(i)
                if tweets:
                    for j in range(len(tweets) -1 ,max(len(tweets)-10-1,-1),-1):
                        tweet = tweets[j]
                        heapq.heappush(minHeap,(tweet.timeStamp,tweet))
                        if len(minHeap) > 10:
                            heapq.heappop(minHeap)
        result = []
        while minHeap:
            result.append(heapq.heappop(minHeap)[1].tweetId)
        return result[::-1]



        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followeesMap:
            self.followeesMap[followerId] = set()
        self.followeesMap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followeesMap:
            self.followeesMap[followerId].discard(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)