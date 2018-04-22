from flask import Flask, render_template, url_for, request


app = Flask(__name__)



@app.route('/')
def tester():
	return render_template('tester.html')

@app.route('/render_results', methods = ['POST'])
def render_results():
	if request.method == 'POST':
		result = request.form['searchterm']
		
	return render_template('render_results.html', result = result)


