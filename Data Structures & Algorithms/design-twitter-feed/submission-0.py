from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # global time to keep track of tweet order
        # bigger time = more recent tweet
        self.time = 0

        # maps userId -> list of (time, tweetId)
        # example: {1: [(1, 101), (2, 102)]}
        self.tweets = defaultdict(list)

        # maps userId -> set of users they follow
        # example: {1: {2, 3}}
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        # increase time whenever a tweet is posted
        self.time += 1

        # store tweet with current time
        self.tweets[userId].append((self.time, tweetId))

    def follow(self, followerId, followeeId):
        # add followee to follower's set
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        # remove followee if they exist
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

    def getNewsFeed(self, userId):
        # this will store the final answer (tweet IDs)
        res = []

        # max heap (we use negative time to simulate max heap)
        heap = []

        # get all users we care about:
        # - people the user follows
        # - the user themselves
        users = self.following[userId] | {userId}

        # STEP 1: add the MOST RECENT tweet of each user to heap
        for user in users:
            if self.tweets[user]:  # if user has tweets
                # index of most recent tweet
                index = len(self.tweets[user]) - 1

                # get that tweet
                time, tweetId = self.tweets[user][index]

                # push into heap:
                # (-time, tweetId, userId, next_index_to_check)
                heapq.heappush(heap, (-time, tweetId, user, index - 1))

        # STEP 2: build the result (up to 10 tweets)
        while heap and len(res) < 10:
            # get the most recent tweet
            time, tweetId, user, index = heapq.heappop(heap)

            # add tweetId to result
            res.append(tweetId)

            # STEP 3: check if this user has more tweets
            if index >= 0:
                # get the next tweet from same user
                time, tweetId = self.tweets[user][index]

                # push it into heap
                heapq.heappush(heap, (-time, tweetId, user, index - 1))

        return res
