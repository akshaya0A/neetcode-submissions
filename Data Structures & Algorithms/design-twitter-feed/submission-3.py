class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)  
        self.followees = defaultdict(set)  
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        users = self.followees[userId].copy()
        users.add(userId)
        for user in users:
            feed.extend(self.tweets[user])
        feed.sort(reverse=True)
        return [tweetId for time, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

