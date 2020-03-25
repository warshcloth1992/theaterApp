"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import ARRAY


# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions



class Genre(db.Model):
    """Genre of movie."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Genre genre_id={self.genre_id} name={self.name}>"


association_table = db.Table('movies_locations',
                             db.Column('location_id',
                                       db.Integer,
                                       db.ForeignKey('locations.location_id')),
                             db.Column('movie_id',
                                       db.Integer,
                                       db.ForeignKey('movies.movie_id')),
)


class Movie(db.Model):
    """Movie on ratings website."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    genre = db.relationship('Genre', backref='movies')

    # To add locations: movie.locations.append(location); then save as usual using db.session.add/commit
    locations = db.relationship('Location',
                                secondary='movies_locations')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Movie movie_id={self.movie_id} title={self.title} genre={self.genre} locations={self.locations}"


class Location(db.Model):
    """Location of a user."""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    name = db.Column(db.String())
    # TODO: Make sure this is a full url with http:// appended, otherwise must add this in templates manually!
    href = db.Column(db.String(2000))
    movies = db.relationship('Movie',
                             secondary='movies_locations')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Location location_id={self.location_id} latitude={self.latitude} longitude={self.longitude} name={self.name}>"


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///moviedb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
