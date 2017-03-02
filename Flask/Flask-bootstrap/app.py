from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_babel import Babel, gettext
from flask import url_for as flask_url_for
from flask import g

app = Flask(__name__)
bootstrap = Bootstrap(app)
babel = Babel(app)
app.debug = True
app.config.from_pyfile('config.py')

@app.before_request
def before():
	if request.view_args and 'lang' in request.view_args:
		if request.view_args['lang'] not in ('en', 'ru'):
			return render_template('404.html')
	if request.view_args and 'lang' in request.view_args:
		g.current_lang = request.view_args['lang']
		request.view_args.pop('lang')

@app.context_processor
def inject_url_for():
    return {
        'url_for': lambda endpoint, **kwargs: flask_url_for(
            endpoint, lang=g.get('current_lang', 'en'), **kwargs
        )
    }

url_for = inject_url_for()['url_for']

@babel.localeselector
def get_locale():
    return g.get('current_lang', 'en')

# @babel.localeselector
# def get_locale():
# 	return 'ru'
	# return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

@app.route('/')
@app.route('/<lang>/')
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

# @app.route('/one')
# def one():
# 	return gettext('Hello')

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html')

if __name__ == '__main__':
	app.run()
