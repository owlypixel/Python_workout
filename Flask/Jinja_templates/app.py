from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']
	weather = {
		'January': {'min': 38, 'max': 47, 'rain': 6.14},
		'February': {'min': 28, 'max': 37, 'rain': 4.54},
		'March': {'min': 58, 'max': 17, 'rain': 8.54},
		'April': {'min': 18, 'max': 77, 'rain': 10.54},
		'May': {'min': 23, 'max': 52, 'rain': 1.22},
		'June': {'min': 23, 'max': 52, 'rain': 1.22},
		'July': {'min': 23, 'max': 52, 'rain': 1.22},
		'August': {'min': 73, 'max': 51, 'rain': 5.22},
		'September': {'min': 11, 'max': 31, 'rain': 5.22},
		'October': {'min': 25, 'max': 67, 'rain': 2.40},
		'November': {'min': 25, 'max': 67, 'rain': 2.40},
		'December': {'min': 25, 'max': 67, 'rain': 2.40}
	}
	highlight = {'min': 40, 'max': 50, 'rain': 6}
	return render_template('index.html', city="Portland, OR", months=months, weather=weather, highlight=highlight)

if __name__ == '__main__':
	app.run()
