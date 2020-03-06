from flask import Flask, render_template
app = Flask(__name__)

genres = {
	"horror" : [
		{
			"name": "It",
			"locations": []
		},
		{
			"name": "Doctor Sleep",
			"locations": []
		}
	],
	"action" : [],
	"romance" : []
}
#data structure holds movies
@app.route('/')
def index():
	return render_template('index.html', genres=genres.keys())
#route to home page from index for genre select element
@app.route('/genre/<g>')
def genre(g=None):
	print(genres.get(g))
	return render_template('genre.html', genre=g)
#route to the data in genres, prints genre selected and returns genre.html template with incerted data


if __name__ == "__main__":
	run.app('0.0.0.0', port=4000)
