CREATE TABLE genres
	(
		genre_id VARCHAR(50),
		PRIMARY KEY (genre_id)
	);

INSERT INTO genres (genre_id) VALUES ('horror')

CREATE TABLE movies
	(
		movie_id VARCHAR(50),
		genre_id VARCHAR(50) REFERENCES genres (genre_id),
		PRIMARY KEY (movie_id)
	);

INSERT INTO movies (movie_id, genre_id) VALUES ('It', 'horror')

CREATE TABLE locations
	(
		location_id VARCHAR(100),
		coordinate POINT,
		name VARCHAR(100),
		PRIMARY KEY (location_id)
	);

INSERT INTO locations (location_id, coordinate, name) VALUES (Point(-93.2650, 44.9778)'minneapolis')	