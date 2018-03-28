from flask import Flask,render_template, url_for, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import tweepy
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

# We define our URL route, and the controller to handle requests
@app.route('/', methods=['GET', 'POST'])
def index():
	form = ReusableForm(request.form)
	print (form.errors)
	if request.method == 'POST':
		tweets=request.form['tweets']
		#print (tweets)
		if form.validate():
            # Save the comment here.
			for tweet in tweepy.Cursor(api.search,q=tweets).items(5):
				flash(tweet.text)
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

