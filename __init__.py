from flask import Flask,render_template, url_for, flash, request, send_file, make_response
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import tweepy
from .sentiment import TwitterClient
from .wordcount import WordCount
from .map_bar import data_vis
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from io import BytesIO
import os
import operator

# Instantiate our app...
# Name it the '__name__' of this module (tweet-harvest)
app = Flask(__name__)

auth = tweepy.OAuthHandler("iHTvDAptJAx3PwfYfw00Qa6sX", "6Gp8kYPR3kULcPPdW3k1gYopQEi4NBdSfFPP8ifHCE0gwkQWCX")
auth.set_access_token("938932912870658048-ICcR2mOBhIvNtIQmMSVdtuQbUsCxIXL", "QU7ArtcKW1aEQYcf0HlMUpS7m07UtQmUNl42OvAJyZ5SH")

api = tweepy.API(auth)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

#@app.template_filter('autoversion')
#def autoversion_filter(filename):
  # determining fullpath might be project specific
#  fullpath = os.path.join('app/', filename[1:])
#  try:
#      timestamp = str(os.path.getmtime(fullpath))
#  except OSError:
#      return filename
#  newfilename = "{0}?v={1}".format(filename, timestamp)
#  return newfilename

class ReusableForm(Form):
        tweets = TextField('SearchField:')

def sentiment(userinput):
    # creating object of TwitterClient Class
    api = TwitterClient(userinput)
    # calling function to get tweets
    #searchterm = input("Enter query: ")
    tweets = api.get_tweets(query=api.searchterm, count=50)

    term  =api.searchterm

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    ptweetstext = ''
    for tweet in ptweets:
        ptweetstext += tweet["text"]

    wordFreq = WordCount(ptweetstext).wordCount

    #print("Top 10 most frequent words in positive tweets: " + getFrequentWordsFrom(ptweets))
    # percentage of positive tweets
    x = 100 * len(ptweets) / len(tweets)
    
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    ntweet_render = []
    count = 0
    for tweet in ntweets:
        if count < 5:
            ntweet_render.append(tweet)
            count += 1

    ptweet_render = []
    count = 0
    for tweet in ptweets:
        if count < 5:
            ptweet_render.append(tweet)
            count += 1

    print("NUMBER OF CONSTRAINED TWEETS:\n")
    print(len(ntweet_render))
    print("\n\n")

    
    # percentage of negative tweets
    y = (100 * len(ntweets) / len(tweets))
    
    # percentage of neutral tweets
    #leftoverTweets = tweets - ntweets - ptweets
    z = (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
    
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [x,y,z]
    colors = ['gold', 'pink', 'lightskyblue']
    explode = (0, 0, 0)  # explode 1st slice
    # Plot
    plt.axis('equal')
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.savefig('static/ah.png')
    plt.close("all")
    
    # Convert sentiments analysis stats to string so they can be displayed as HTML
    ptweet_analyses = "Positive tweets:" + str(x) + "%"
    ntweets_analyses = "Negative tweets:" + str(y) + "%"
    nut_tweet_analyses = "Neutral tweets:" + str(z) + "%"

    data_vis(tweets, ptweets, ntweets, term)

    return ptweets, ptweet_render,ntweets, ntweet_render, ptweet_analyses, ntweets_analyses, nut_tweet_analyses, wordFreq


# We define our URL route, and the controller to handle requests
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
    return render_template('index.html', form = form)

@app.route('/render_Data', methods = ['GET', 'POST'])
def render_Data():
    if request.method == 'POST':
        tweets=request.form['tweets']
        ptweets, ptweet_render,ntweets, ntweet_render, ptweet_analyses, ntweets_analyses, nut_tweet_analyses, wordFreq = sentiment(tweets)
        
    return render_template('render_Data.html', ptweet_render = ptweet_render, ntweet_render = ntweet_render, ptweet_analyses = ptweet_analyses,
    ntweets_analyses = ntweets_analyses, nut_tweet_analyses = nut_tweet_analyses, wordFreq = wordFreq)


@app.route('/ContactUs', methods = ['GET', 'POST'])
def ContactUs():
    return render_template('ContactUsNew.html')

@app.route('/About')
def AboutProject():
    return render_template('about_project.html')

@app.route('/Results')
def Results():
    #def get_Tweets(wordSearch):
        #wordSearch = input("What's input do you want to search for? ")
    #print("This is your input: " + wordSearch )
        
            #print(tweet.text)
    return render_template('results.html')