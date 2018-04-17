# sentiment analysis pie chart
import matplotlib.pyplot as plt
# line means plt= matplotlib.pyplor
import matplotlib.animation as animation

#from sentiment.py

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

#Most code borrowed from https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
#Slightly modified, original borrowed code actually doesn't compile without slight modifications

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'iHTvDAptJAx3PwfYfw00Qa6sX'
        consumer_secret = '6Gp8kYPR3kULcPPdW3k1gYopQEi4NBdSfFPP8ifHCE0gwkQWCX'
        access_token = '938932912870658048-ICcR2mOBhIvNtIQmMSVdtuQbUsCxIXL'
        access_token_secret = 'QU7ArtcKW1aEQYcf0HlMUpS7m07UtQmUNl42OvAJyZ5SH'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    searchterm = input("Enter query: ")
    tweets = api.get_tweets(query=searchterm, count=10)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    x=(100 * len(ptweets) / len(tweets))
    print("positive")
    print (x)

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    y=(100 * len(ntweets) / len(tweets))
    # percentage of neutral tweets
    #leftoverTweets = tweets - ntweets - ptweets
    print("negative")
    print(y)
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))
    z=(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
    print("neutral")
    print(z)

    # this is just how you start creating a pie chart
    #here you create the slice names, the sizes and colors for the slices
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [x, y, z]
    colors = ['gold', 'pink', 'lightskyblue']
    explode = (0, 0, 0)  # explode 1st slice
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()



if __name__ == "__main__":
    # calling main function
    main()

