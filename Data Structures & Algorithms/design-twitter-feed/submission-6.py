class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)  
        self.followees = defaultdict(set)  
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.followees[userId].copy()
        users.add(userId)
        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap, (time, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [tweetId for time, tweetId in sorted(heap, reverse=True)]
 


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

