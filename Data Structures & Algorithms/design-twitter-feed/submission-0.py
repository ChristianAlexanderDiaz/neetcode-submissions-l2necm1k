from collections import defaultdict
from typing import List
class Twitter:

    def __init__(self):
        self.adjList = defaultdict(list)
        self.relationships = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.adjList[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.relationships[userId] | {userId}
        combined = []
        for u in users:
            combined.extend(self.adjList[u])
        return [tid for _, tid, in sorted(combined, reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.relationships[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.relationships[followerId].discard(followeeId)
        
