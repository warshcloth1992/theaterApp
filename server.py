from flask import Flask, render_template
app = Flask(__name__)

genres = {
	"horror" : [],
	"action" : [],
	"romance" : []
}

@app.route('/')
def index():
	return render_template('index.html', genres=genres.keys())

@app.route('/genre/<g>')
def genre(g=None):
	return render_template('genre.html')


if __name__ == "__main__":
	run.app('0.0.0.0', port=4000)
