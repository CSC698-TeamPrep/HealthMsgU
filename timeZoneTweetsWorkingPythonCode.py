# TO USE TO GET TIME ZONES
# THIS CODE WORKS WAHOO



# print("hello world")
#
# import tweepy
#
# auth = tweepy.OAuthHandler("iHTvDAptJAx3PwfYfw00Qa6sX", "6Gp8kYPR3kULcPPdW3k1gYopQEi4NBdSfFPP8ifHCE0gwkQWCX")
# auth.set_access_token("938932912870658048-ICcR2mOBhIvNtIQmMSVdtuQbUsCxIXL", "QU7ArtcKW1aEQYcf0HlMUpS7m07UtQmUNl42OvAJyZ5SH")
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#    print(tweet.text)
#    #*Task two:* You've got Python and Tweepy running on your machine -- now write a Python script that scrapes
#    # Twitter for posts about a query that you provide!
#    #  If you can, have your script output a couple of datums for the posts you scrape -- the username of the poster, the date, etc.
#





# to make a better search
#asking what the user wants to search for
wordSearch = input("What's input do you want to search for? ")
print("This is your input: " + wordSearch )

#word="dum"
#if wordSearch in word:
 #  print('Success!')

import tweepy

auth = tweepy.OAuthHandler("iHTvDAptJAx3PwfYfw00Qa6sX", "6Gp8kYPR3kULcPPdW3k1gYopQEi4NBdSfFPP8ifHCE0gwkQWCX")
auth.set_access_token("938932912870658048-ICcR2mOBhIvNtIQmMSVdtuQbUsCxIXL", "QU7ArtcKW1aEQYcf0HlMUpS7m07UtQmUNl42OvAJyZ5SH")

api = tweepy.API(auth)


#items say number of tweets looked at
for tweet in tweepy.Cursor(api.search,q=wordSearch).items(20):
    # just print(tweet.text) for the results (tweet.author or dae)
    # just print(tweet) for all the results

    x=tweet.author
    y=x.time_zone

    print(y)
    #print(tweet.text)
    # x.geo_enabled works0