from flask import Flask

app = Flask('app')
app.debug = True

@app.route('/')
def homepage():
	with open('home.html') as file:
		response = file.read()
	return response

@app.route('/page/1')
def page1():
	with open('page1.html') as file:
		response = file.read()
	return response

@app.route('/page/2')
def page2():
	with open('page2.html') as file:
		response = file.read()
	return response

if __name__ == '__main__':
	app.run()
