""" """

from jinja2 import StrictUndefined
from sqlalchemy.schema import Sequence 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.orm.exc import NoResultFound

from model import connect_to_db, db, Genre, Movie, Location
app = Flask(__name__)
#needed to use debugger
app.secret_key = "ABC"


app.jinja_env.undefined = StrictUndefined

# route to home page from index for genre select element
@app.route('/')
def index():
	genres= Genre.query.all()
	return render_template('index.html', genres=genres,)


@app.route('/new-movie', methods=['POST'])
def new_movie():
	print("here")
	payload = request.form.to_dict()
	title = payload.get('movie')
	genre = Genre.query.filter_by(name=payload.get('genre')).first()
	if genre is None:	
		return 'unknown genre'
	print(genre)
	genre_id = genre.genre_id
	movie = Movie(title=title,
                  genre_id=genre_id)
	db.session.add(movie)
	db.session.commit()
	return 'success'	


# add route to handle search by movie and location
@app.route('/genre/<mygenre>')
def genre(mygenre=None):
	movies = Movie.query.filter_by(genre_id=mygenre).all()
	print(movies)
	return render_template('genre.html', genres=movies)

 




if __name__ == "__main__":
	app.debug = True
	connect_to_db(app)
	DebugToolbarExtension(app)

	app.run('0.0.0.0', port=4000)
