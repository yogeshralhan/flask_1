from flask import Flask
app = Flask(__name__)

@app.route('/home')
def index():
	return '<h1> Hello World </h1>  <body> hello to the new web app <a href="http://www.w3schools.com">This is a link</a></body>  <h2> Python Basics</h2>'

if __name__== '__main__':
	app.run(debug=True)

