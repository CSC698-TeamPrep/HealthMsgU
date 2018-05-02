#proof of concept which displays the most frequently used words in a string

import tweepy

auth = tweepy.OAuthHandler("iHTvDAptJAx3PwfYfw00Qa6sX", "6Gp8kYPR3kULcPPdW3k1gYopQEi4NBdSfFPP8ifHCE0gwkQWCX")
auth.set_access_token("938932912870658048-ICcR2mOBhIvNtIQmMSVdtuQbUsCxIXL", "QU7ArtcKW1aEQYcf0HlMUpS7m07UtQmUNl42OvAJyZ5SH")

wordSearch = input("What input do you want to search for? ")
print("This is your input: " + wordSearch )

api = tweepy.API(auth)
TotalTweet = " "

for tweet in tweepy.Cursor(api.search,q=wordSearch).items(100):
        TotalTweet+= tweet.text
        #print(TotalTweet)

import operator


def counter(l):
    result = {}
    for word in l:
        result.setdefault(word, 0)
        result[word] += 1

    return result


def h(s):
    scores = counter(s.split())
    scores = sorted(scores.items(), key=operator.itemgetter(1))
    scores = reversed(scores)
    scores = list(x[0] for x in scores)
    return scores[0:10]

print(h(TotalTweet))