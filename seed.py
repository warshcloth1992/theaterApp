"""Utility file to seed ratings database from MovieLens data in seed_data/"""


from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

from model import Genre, Movie, connect_to_db, db, Location
from server import app

from faker import Faker

faker = Faker()

def create_googlemaps_href(longitude, latitude):
    return 'https://www.google.com/maps/place/' + str(longitude) + '+' + str(latitude)


def init_db():
    """Clear existing data and create new tables."""
    db = SQLAlchemy()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def create_fake_movies():
    """A short example of how to use faker"""

    genre_id = Genre.query.get(1)
    location = Location.query.get(1)
    for i in range(100):
        movie = Movie(title=faker.sentence(nb_words=2), genre_id=genre_id)
        movie.locations.append(location)
        db.session.add(movie)
        db.session.commit()


def load_genres(genre_filename):
    """Load users from u.user into database."""

    print("Genres")

    for i, row in enumerate(open(genre_filename)):
        row = row.rstrip()
        
        genre_id, name = row.split("|")

        genre = Genre(genre_id=int(genre_id),
                      name=name)

        # add session to add data
        db.session.add(genre)

    #commit data
    db.session.commit()


def load_movies(movie_filename):
    """Load movies from movie_filename.txt into database."""

    print("Loading movies...")
    #map txt information to movie model and insert split rows into database
    for i, row in enumerate(open(movie_filename)):
        row = row.rstrip()

        movie_id, title, genre_id, location_id = row.split("|")

        movie = Movie(movie_id=movie_id,
                      title=title,
                      genre_id=genre_id)
        location = Location.query.filter_by(location_id=location_id).one()
        movie.locations.append(location);

        # We need to add to the session or it won't ever be stored
        db.session.add(movie)
    # Once we're done, we should commit our work
    db.session.commit()

def load_locations(location_filename):
    """Load locations from location_filename.txt into database."""

    print('Loading locations...')

    for i, row in enumerate(open(location_filename)):
        row = row.rstrip()

        location_id, latitude, longitude, name = row.split("|")

        location = Location(location_id=location_id,
                            latitude=latitude,
                            longitude=longitude,
                            name=name,
                            href=create_googlemaps_href(latitude, longitude))
        db.session.add(location)
    db.session.commit()    


# connects my computer to the database, initializes tables, and inserts seeded data into tables
if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    genre_filename = "seed_data/genre_seed.txt"
    movie_filename = "seed_data/movie_seed.txt"
    location_filename = "seed_data/location_seed.txt"

    load_genres(genre_filename)
    load_locations(location_filename)
    load_movies(movie_filename)
