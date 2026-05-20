import heapq
from collections import defaultdict

class Tweets:
    def __init__(self, id: int, time: int) -> None:
        self.id = id
        self.time = time

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(Tweets(tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        q = []
        users = {userId} | self.follows[userId]
        for user in users:
            for tweet in self.tweets[user][-10:]:
                heapq.heappush(q, (tweet.time, tweet.id))
                # the min num is invalid, we need newest num
                if len(q) > 10:
                    heapq.heappop(q)
        return [t[1] for t in sorted(q, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
