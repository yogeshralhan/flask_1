
from flask import Flask     #  Import statment---> package flask   module ----> Flask
app = Flask(__name__)		#  __name__    ---> directory or root path for web application to start

@app.route('/user/<name>')    	# path to specify location on system
def user(name):								#pass the parameter....dynamic 
	return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':    # main call
	app.run(debug=True)