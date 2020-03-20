""" """

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Genre, Movie, Location
app = Flask(__name__)

app.secret_key = "ABC"
#needed to use debugger

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	genres= Genre.query.all()
	return render_template('index.html', genres=genres,)
# route to home page from index for genre select element, why cant i add the css file
# @app.route('/genre/')


@app.route('/genre/<mygenre>')
def genre(mygenre=None):
	movies = Movie.query.filter(Movie.genre_id == mygenre).all()

	return render_template('genre.html', genres=movies)

# what movies have been playing this year
# can they search by title or location 
# think about different ways to interact 


# @app.route('/genres'/'movies'/'locations')
# def show_all_genres():

# 	# Genre.query.filter(name == 'SciFi').first()
# 	genres = Genre.query.all()
# 	first = Genre.query.first()

# 	return render_template('genres.html', genres=genres, first=first)
# route to the data in genres, prints genre selected and returns genre.html template with incerted data
# @app.route('new page?')
# def location
# return render_template('', )


if __name__ == "__main__":
	app.debug = True
	connect_to_db(app)
	DebugToolbarExtension(app)

	app.run('0.0.0.0', port=4000)
