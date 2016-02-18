from flask import Flask
app= Flask(__name__)

@app.route('/home')
def index():
	return '<h1> Hello World</h1>     <h2> Hello </h2>'

@app.route('/home/<n>')
def name1(n):
	return '<h3>name is %s<h3>' %n

if __name__== '__main__':
	app.run(debug=True)
