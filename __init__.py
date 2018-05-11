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


app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


#Generates Form to be rendered on render_data.html
class ReusableForm(Form):
        tweets = TextField('Search Health Term:')

#This function performs sentiment analyses on the twitter data as well as calls methods for additional data analyses
def sentiment(userinput):
    # creating object of TwitterClient Class
    api = TwitterClient(userinput)
    # calling function to get tweets
    #searchterm = input("Enter query: ")
    tweets = api.get_tweets(query=api.searchterm, count=50)

    term  =api.searchterm

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    #stores tweets in variable to be passed to wordCount()
    tweetstext = ''
    for tweet in tweets:
        tweetstext += tweet["text"]

    #Calculates word frequency in all tweets
    wordFreq = WordCount(tweetstext).wordCount

    #print("Top 10 most frequent words in positive tweets: " + getFrequentWordsFrom(ptweets))
    # percentage of positive tweets
    x = 100 * len(ptweets) / len(tweets)
    
    # percentage of negative tweets
    y = (100 * len(ntweets) / len(tweets))
    
    # percentage of neutral tweets
    #leftoverTweets = tweets - ntweets - ptweets
    z = (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
    


    #creates a list of positive tweets to be displayed on render_data.html
    ptweet_render = []
    count = 0
    for tweet in ptweets:
        if count < 5:
            ptweet_render.append(tweet)
            count += 1

    #Creates a list of negative tweets to be displayed on render_data.html
    ntweet_render = []
    count = 0
    for tweet in ntweets:
        if count < 5:
            ntweet_render.append(tweet)
            count += 1

    #For debugging
    #print("NUMBER OF CONSTRAINED TWEETS:\n")
    #print(len(ntweet_render))
    #print("\n\n")

    #Code to generate pie chart
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
    #ptweet_analyses = "Positive tweets:" + str(x) + "%"
    #ntweets_analyses = "Negative tweets:" + str(y) + "%"
    #nut_tweet_analyses = "Neutral tweets:" + str(z) + "%"
    
    #Calls data_vis function for additional data vis elements
    data_vis(tweets, ptweets, ntweets, term)


    return term, ptweets, ptweet_render, ntweets, ntweet_render, wordFreq




# We define our URL route, and the controller to handle requests
@app.route('/', methods=['GET', 'POST'])
def index():
	#Create form object to be rendered on index.html
    form = ReusableForm(request.form)
    return render_template('index.html', form = form)

@app.route('/render_Data', methods = ['GET', 'POST'])
def render_Data():
	#When the form is submitted text from the text field passed to a variable
    if request.method == 'POST':
        tweets=request.form['tweets']
        #Calling sentiment.py method to pull tweets from twitter and perform sentiment analyses along with other data vis
        term, ptweets, ptweet_render,ntweets, ntweet_render, wordFreq = sentiment(tweets)
        
    return render_template('render_Data.html', term = term, ptweet_render = ptweet_render, ntweet_render = ntweet_render,
    wordFreq = wordFreq)



@app.route('/ContactUs', methods = ['GET', 'POST'])
def ContactUs():
    return render_template('ContactUsNew.html')

@app.route('/About')
def AboutProject():
    return render_template('about_project.html')
