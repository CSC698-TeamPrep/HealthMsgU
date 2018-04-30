from flask import Flask,render_template, url_for, flash, request, send_file, make_response
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import tweepy
from .sentiment import TwitterClient
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from io import BytesIO
import os

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
    tweets = api.get_tweets(query=api.searchterm, count=10)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    ptweet_analyses_pie = 100 * len(ptweets) / len(tweets)
    
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    ntweets_analyses_pie = (100 * len(ntweets) / len(tweets))
    
    # percentage of neutral tweets
    #leftoverTweets = tweets - ntweets - ptweets
    nut_tweet_analyses_pie = (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
    
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [ptweet_analyses_pie,nut_tweet_analyses_pie,ntweets_analyses_pie]
    colors = ['gold', 'pink', 'lightskyblue']
    explode = (0, 0, 0)  # explode 1st slice
    # Plot
    plt.axis('equal')
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.savefig('static/ah.png')
    plt.close("all")
    
    # Convert sentiments analysis stats to string so they can be displayed as HTML
    ptweet_analyses = "Positive tweets:" + str(ptweet_analyses_pie) + "%"
    ntweets_analyses = "Negative tweets:" + str(ntweets_analyses_pie)
    nut_tweet_analyses = "Neutral tweets:" + str(nut_tweet_analyses_pie) + "%"

    return ptweets, ntweets, ptweet_analyses, ntweets_analyses, nut_tweet_analyses


# We define our URL route, and the controller to handle requests
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
    return render_template('index.html', form = form)

@app.route('/render_Data', methods = ['GET', 'POST'])
def render_Data():
    if request.method == 'POST':
        tweets=request.form['tweets']
        ptweets, ntweets, ptweet_analyses, ntweets_analyses, nut_tweet_analyses = sentiment(tweets)
        
    return render_template('render_Data.html', ptweets = ptweets, ntweets = ntweets, ptweet_analyses = ptweet_analyses,
    ntweets_analyses = ntweets_analyses, nut_tweet_analyses = nut_tweet_analyses)


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