DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INT,
    duration INT
);
