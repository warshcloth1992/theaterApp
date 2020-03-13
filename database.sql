CREATE TABLE genres
	(
		genre_id VARCHAR(50) NOT NULL,
		PRIMARY KEY (genre_id)
	);

INSERT INTO genres (genre_id) 
VALUES ('horror');



CREATE TABLE movies
	(
		movie_id VARCHAR(50) NOT NULL,
		genre_id VARCHAR(50) NOT NULL 
		REFERENCES genres (genre_id),
		PRIMARY KEY (movie_id)
	);

INSERT INTO movies (movie_id, genre_id) 
VALUES ('It', 'horror');




CREATE TABLE locations
	(
		location_id INT NOT NULL,
		coordinate POINT NOT NULL,
		name VARCHAR(100) NOT NULL,
		PRIMARY KEY (location_id)
	);

INSERT INTO locations (location_id, coordinate, name) 
VALUES (1, Point(-93.2650, 44.9778),'theater');	