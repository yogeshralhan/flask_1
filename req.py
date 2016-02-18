from flask import Flask
app = Flask(__name__)


@app.route('/home')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent

@app.route('/home/name')
def name(n):
	return '<h1>name is %s<h3>' %n

if __name__ == '__main__':
	app.run(debug=True)