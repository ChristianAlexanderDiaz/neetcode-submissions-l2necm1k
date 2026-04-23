class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followings = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followings[userId] | {userId}
        combined = []
        for u in users:
            combined.extend(self.tweets[u])

        return [tweetId for _, tweetId in sorted(combined, reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)
