"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

# new_user = User(email='hello@balloonicorn.com', password='rainbows_are_best', age='35', zipcode='55403')
# new_user.email
# 'hello@ballonicorn.com'
# SELECT email FROM USERS WHERE user_id = 1;

class Genre(db.Model):
    """Genre of movie."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Genre genre_id={self.genre_id} name={self.name}>"


class Movie(db.Model):
    """Movie on ratings website."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    title = db.Column(db.String(100))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    
    genre = db.relationship('Genre', backref='movies')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Movie movie_id={self.movie_id} title={self.title} genre={self.genre}>"


class Location(db.Model):
    """Location of a user."""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)
    latitude = db.Column(db.Float)
    longetude = db.Column(db.Float)
    name = db.Column(db.String())

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Location location_id={self.location_id} latitude={self.latitude} longitude={self.longitude} name={self.name}>"


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies'
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
