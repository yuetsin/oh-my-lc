#!/usr/bin/env python


class Tweet:
    def __init__(self, tweetId, userId):
        self.tweetId = tweetId
        self.userId = userId
        # self.sentTime = time


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.globalTime = 0
        self.tweets = []
        self.userFollows = {}

#     def getTime(self):
#         self.globalTime += 1
#         return self.globalTime

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.insert(0, Tweet(tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId in self.userFollows:
            followings = self.userFollows[userId]
        else:
            followings = set()
        counts = 0
        filteredTweets = []

        for tweet in self.tweets:
            if tweet.userId in followings or tweet.userId == userId:
                filteredTweets.append(tweet.tweetId)
                counts += 1
                if counts >= 10:
                    return filteredTweets

        return filteredTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.userFollows:
            self.userFollows[followerId].add(followeeId)
        else:
            self.userFollows.update({
                followerId: set()
            })
            self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.userFollows:
            try:
                self.userFollows[followerId].remove(followeeId)
            except:
                pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
