from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ContactUs')
def ContactUs():
	return render_template('ContactUsNew.html')

@app.route('/About')
def AboutProject():
	return render_template('about_project.html')

@app.route('/Results')
def Results():
	return render_template('results.html')

