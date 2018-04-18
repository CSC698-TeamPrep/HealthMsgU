from flask import Flask,render_template, url_for, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import tweepy
from .sentiment import TwitterClient
# Instantiate our app...
# Name it the '__name__' of this module (tweet-harvest)
app = Flask(__name__)

auth = tweepy.OAuthHandler("iHTvDAptJAx3PwfYfw00Qa6sX", "6Gp8kYPR3kULcPPdW3k1gYopQEi4NBdSfFPP8ifHCE0gwkQWCX")
auth.set_access_token("938932912870658048-ICcR2mOBhIvNtIQmMSVdtuQbUsCxIXL", "QU7ArtcKW1aEQYcf0HlMUpS7m07UtQmUNl42OvAJyZ5SH")

api = tweepy.API(auth)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    	tweets = TextField('SearchField:', validators=[validators.required()])

def sentiment(userinput):
    # creating object of TwitterClient Class
    api = TwitterClient(userinput)
    # calling function to get tweets
    #searchterm = input("Enter query: ")
    tweets = api.get_tweets(query=api.searchterm, count=10)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    flash("<h1>Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)) + "</h1>")
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    flash("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets
    #leftoverTweets = tweets - ntweets - ptweets
    print("Neutral tweets percentage: {} % \ ".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])

# We define our URL route, and the controller to handle requests
@app.route('/', methods=['GET', 'POST'])
def index():
	form = ReusableForm(request.form)
	print (form.errors)
	if request.method == 'POST':
		tweets=request.form['tweets']
		sentiment(tweets)
		#print (tweets)
		if form.validate():
			for tweet in tweepy.Cursor(api.search,q=tweets).items(5):
				flash(tweet)
		else:
			flash('All the form fields are required. ')
	return render_template('index.html', form = form)

@app.route('/ContactUs')
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
