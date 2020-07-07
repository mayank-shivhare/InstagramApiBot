import datetime
import random
import time
from threading import Thread

from InstagramAPI import InstagramAPI

username = ""
password = ""

NumberOfLikes = 150
NumberOfComment = 20
NumberofFollow = 20
MaxTimeLike = 1 * 30 * 60  ################2 stands for hours
MaxTimeComment = 1 * 30 * 60  ################2 stands for hours

api = InstagramAPI(username, password)


def Login():
    api.login()


def Logout():
    api.logout()


def Time():
    x = datetime.datetime.now()
    print(x.strftime("%X"))


commentList = [
    "Your Feeds are awesome",
    "That's a lovely Click :)",
    "Love This",
    "Awesome",
    "Nice Click",
    "Wow",
    "This is really Cool",
    "Well Captured",
    "This looks amazing",
    "Your content is awesome. Feel Free to look mine",
    "Your content is awesome, please have a look at mine content and give me some feedback :)",
    "Amazingly caputed, looking forward for more feeds like this",
    "Good job! You are going to be very famous",
    "Hey! you photos are getting better with time",
    "Captured Perfectly :)",
    "Hey! Good going you have one of the best galleries I have seen today. Do check mine too :)",
    "Amazing, Keep it up",
    "The best of the best",
]


def PopularFeeds(WhatPopularFeed):
    api.getPopularFeed()
    feed = api.LastJson
    # print(feed)
    if (WhatPopularFeed == "user_id"):  ###### This will return Popular user_id
        ListOfPopularUserid = []
        for items in feed["items"]:
            for caption in items:
                if caption == "caption":
                    try:
                        UserID = (items[caption]['user_id'])
                        # print("user_id %s" % UserID)
                        int(UserID)
                        ListOfPopularUserid.append(UserID)
                    except:
                        # print("Cant get user_id")
                        print("")

        # print("This is the list of user_id that is getting returned %s" % ListOfPopularUserid)
        return ListOfPopularUserid

    if (WhatPopularFeed == "media_id"):  ###### This will return Popular media_id
        ListOfMediaId = []
        for items in feed["items"]:
            for caption in items:
                if caption == "caption":
                    try:
                        MediaId = (items[caption]['media_id'])
                        # print("Media_id %s" % MediaId)
                        int(MediaId)
                        ListOfMediaId.append(MediaId)
                    except:
                        # print("Cant get media id")
                        print("")

        # print("This is the list of media id that is getting returned %s" % ListOfMediaId)
        return ListOfMediaId


def MyFollowingFeeds():
    api.timelineFeed()
    feed = api.LastJson
    ListOfMyFollowingFeeds = []
    for items in feed["items"]:
        for caption in items:
            if caption == "caption":
                try:
                    MediaId = (items[caption]['media_id'])
                    # print("Media_id %s" % MediaId)
                    int(MediaId)
                    ListOfMyFollowingFeeds.append(MediaId)
                except:
                    # print("Cant get media id")
                    print("")

    # print("This is the list of user_id that is getting returned %s" % ListOfMyFollowingFeeds)
    return ListOfMyFollowingFeeds


def Like(MediaToLike):
    try:
        api.like(mediaId=MediaToLike)
        print("Liking Media %i" % MediaToLike)
        time.sleep(2)
    except:
        print("Cant Like Media %i" % MediaToLike)


def Comment(MediaToComment, CommentData):
    try:
        api.comment(MediaToComment, CommentData)
        print("commenting %i %s" % (MediaToComment, CommentData))
    except:
        print("Unable to comment %i %s" % (MediaToComment, CommentData))


def Follow(user_id):
    try:
        api.follow(user_id)
        print("Following %i" % user_id)
    except:
        print("Unable to follow user %i" % user_id)


def Unfollow(user_id):
    try:
        api.unfollow(user_id)
        print("Unfollowing %i" % user_id)
    except:
        print("Cant Unfollow %i" % user_id)


def GetFollowerlist():
    api.getTotalSelfFollowers()
    follower = api.LastJson
    usernameList = []

    for user in follower['users']:
        usernameOfFollower = (user['username'])
        usernameList.append(usernameOfFollower)
    return usernameList


def GetFollowingList():
    api.getTotalSelfFollowings()
    following = api.LastJson
    followingList = []

    for user in following['users']:
        usernameOfFollowing = (user['username'])
        followingList.append(usernameOfFollowing)
    return followingList


class Like_logic(Thread):
    def run(self):
        likeNumber = 0
        while likeNumber <= NumberOfLikes:
            i = 0
            while i <= random.randint(10, 15):
                popularfeed = PopularFeeds("media_id")
                randomPopularFeedForLike = random.sample(popularfeed, 1)
                Like(randomPopularFeedForLike[0])
                likeNumber += 1
                i += 1

                print("Like Number %i" % likeNumber)  # Sleeping for min 3 and max 10 seconds
                time.sleep(random.randint(3, 10))  # Sleeping between two likes

                followingFeeds = MyFollowingFeeds()
                randomFollowingFeedForLike = random.sample(followingFeeds, 1)
                Like(randomFollowingFeedForLike[0])
                likeNumber += 1
                print("Like Number %i" % likeNumber)
                i += 1

                sleepingtime = random.randint(60, 120)  # sleeping for min 1  max 2 minutes
                # sleepingtime = random.randint(6, 12)  # sleeping for min 1  max 2 minutes
                print("Sleeping for %i" % sleepingtime)  # sleeping time between two likes
                time.sleep(sleepingtime)

            print(likeNumber)
            sleepingtime = random.randint(1800, 3600)  # sleep of 30 minutes to 1 hour between 1 cycle
            # sleepingtime = random.randint(18, 36)  # sleep of 30 minutes to 1 hour between 1 cycle
            print("Sleeping for %i" % sleepingtime)
            time.sleep(sleepingtime)


class Comment_logic(Thread):
    def run(self):
        commentNumber = 0
        while commentNumber <= NumberOfComment:
            popularfeed = PopularFeeds("media_id")
            randomPopularFeedForComment = random.sample(popularfeed, 1)
            randomComment = random.sample(commentList, 1)

            formattedComment = str(randomComment[0])
            Comment(randomPopularFeedForComment[0], formattedComment)
            commentNumber += 1
            print("Comment Number %i" % commentNumber)

            print(commentNumber)
            sleepingtime = random.randint(1800, 2400)  # sleeping for 30-40 minutes between each comment
            # sleepingtime = random.randint(18, 24)  # sleeping for 30-40 minutes between each comment
            print("Sleeping for %i" % sleepingtime)
            time.sleep(sleepingtime)


class Follow_logic(Thread):
    def run(self):
        followNumber = 0
        while followNumber <= NumberofFollow:
            popularUser = PopularFeeds("user_id")
            randomPopularFeedForFollow = random.sample(popularUser, 1)
            Follow(randomPopularFeedForFollow[0])
            followNumber += 1
            print("Follow Number %i" % followNumber)

            print(followNumber)
            sleepingtime = random.randint(1800, 2400)  # sleeping for 30-40 minutes between each Follow
            # sleepingtime = random.randint(18, 24)  # sleeping for 30-40 minutes between each Follow
            print("Sleeping for %i" % sleepingtime)
            time.sleep(sleepingtime)


if __name__ == '__main__':
    Login()
    # api.getRecentActivity()

    # get_recent_activity_response = api.LastJson
    # # for notifcation in get_recent_activity_response['old_stories']:
    # #     print (notifcation['args']['text'])
    # print(get_recent_activity_response)

    #badal ki user id nikali 6663148905
    # api.getUserFeed(usernameId=11527194927,maxid=1)
    # abc=api.LastJson
    # print(abc)
    Like(1996364822698813344)

    # try:
    #     Login()
    #     print(Time())
    #     t1 = Like_logic()
    #     t2 = Comment_logic()
    #     t3 = Follow_logic()
    #
    #     t1.start()
    #     t2.start()
    #     t3.start()
    #
    #     t1.join()
    #     t2.join()
    #     t3.join()
    #
    #     print(Time())
    #     print("Logging Out")
    #     Logout()
    #     input("Program has ended")
    # except:
    #
    #     print(Time())
    #     print("Logging Out")
    #     Logout()
    #     input("Program has ended")
