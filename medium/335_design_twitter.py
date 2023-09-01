# https://leetcode.com/problems/design-twitter/description/

from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.timestamp = {}
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] += [tweetId]
        self.timestamp[tweetId] = self.counter
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []
        for id in self.follows[userId]:
            for tid in self.tweets[id]:
                heapq.heappush(hp, (self.timestamp[tid], tid))

                if len(hp) > 10:
                    heapq.heappop(hp)
        for tid in self.tweets[userId]:
            heapq.heappush(hp, (self.timestamp[tid], tid))

            if len(hp) > 10:
                heapq.heappop(hp)
        return [heapq.heappop(hp)[1] for _ in range(len(hp))][::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)