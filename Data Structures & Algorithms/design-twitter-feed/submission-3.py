from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.userPosts = defaultdict(list)
        self.cnter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPosts[userId].append((-self.cnter, tweetId))
        self.cnter+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        userIds = set([userId])
        for follower_id in self.follow_map[userId]:
            userIds.add(follower_id)
        heap = []
        for usr in userIds:
            for cnt, tweetid in self.userPosts[usr]:
                heapq.heappush(heap, (cnt, tweetid))
        res = []
        while heap and len(res) < 10:
            cnt, new = heapq.heappop(heap)
            res.append(new)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

