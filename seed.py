"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime
from sqlalchemy import func

from model import Genre, Movie, connect_to_db, db
from server import app


def load_genres(genre_filename):
    """Load users from u.user into database."""

    print("Genres")

    for i, row in enumerate(open(genre_filename)):
        row = row.rstrip()
        genre_id, name = row.split("|")

        genre = Genre(genre_id=int(genre_id),
                      name=name)

        # We need to add to the session or it won't ever be stored
        db.session.add(genre)

    # Once we're done, we should commit our work
    db.session.commit()


def load_movies(movie_filename):
    """Load movies from u.item into database."""

    print("Movies")

    for i, row in enumerate(open(movie_filename)):
        row = row.rstrip()

        # clever -- we can unpack part of the row!
        movie_id, title, released_str, junk, imdb_url = row.split("|")[:5]

        # The date is in the file as daynum-month_abbreviation-year;
        # we need to convert it to an actual datetime object.

        if released_str:
            released_at = datetime.datetime.strptime(released_str, "%d-%b-%Y")
        else:
            released_at = None

        # Remove the (YEAR) from the end of the title.

        title = title[:-7]   # " (YEAR)" == 7

        movie = Movie(title=title,
                      released_at=released_at,
                      imdb_url=imdb_url)

        # We need to add to the session or it won't ever be stored
        db.session.add(movie)

        # provide some sense of progress
        if i % 100 == 0:
            print(i)

    # Once we're done, we should commit our work
    db.session.commit()


# def load_ratings(rating_filename):
#     """Load ratings from u.data into database."""

#     print("Ratings")

#     for i, row in enumerate(open(rating_filename)):
#         row = row.rstrip()

#         user_id, movie_id, score, timestamp = row.split("\t")

#         user_id = int(user_id)
#         movie_id = int(movie_id)
#         score = int(score)

#         # We don't care about the timestamp, so we'll ignore this

#         rating = Rating(user_id=user_id,
#                         movie_id=movie_id,
#                         score=score)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(rating)

#         # provide some sense of progress
#         if i % 1000 == 0:
#             print(i)

#             # An optimization: if we commit after every add, the database
#             # will do a lot of work committing each record. However, if we
#             # wait until the end, on computers with smaller amounts of
#             # memory, it might thrash around. By committing every 1,000th
#             # add, we'll strike a good balance.

#             db.session.commit()

#     # Once we're done, we should commit our work
#     db.session.commit()


def set_val_genre_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(Genre.genre_id)).one()
    max_id = int(result[0])

    # Set the value for the next genre_id to be max_id + 1
    query = "SELECT setval('genres_genre_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    genre_filename = "ratings/solution/genre_seed.txt"
    movie_filename = "seed_data/u.item"
    rating_filename = "seed_data/u.data"
    load_genres(genre_filename)
    # load_movies(movie_filename)
    # load_ratings(rating_filename)
    set_val_genre_id()
