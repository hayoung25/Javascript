
-- SELECT: Select columns 
SELECT name, genre, year
FROM movies

-- AS: select a column with a new name as ""
SELECT imdb_rating AS 'IMDb'
FROM movies

-- DISTINCT: only select items which are distinct(not same)
SELECT DISTINCT genre
FROM movies;

-- WHERE: giving condition of selection
SELECT * 
FROM movies 
WHERE imdb_rating < 5;

-- LIKE: giving specific condition of selection
SELECT * 
FROM movies
WHERE name LIKE 'Se_en'

-- SELECT * 
FROM movies
WHERE name LIKE '%man%';

-- SELECT * 
FROM movies
WHERE name LIKE 'The %

-- ISNULL: retrieving column which is null
SELECT name
FROM movies
WHERE imdb_rating IS NULL;

-- BETWEEN: literally between 
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979;

-- AND & OR
SELECT *
FROM movies
WHERE year < 1985
   AND genre = 'horror';

SELECT *
FROM movies
WHERE genre = 'romance'
   OR genre = 'comedy';

-- ORDER BY: sort items order by
SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating ASC;

-- LIMIT: retrieve limited number of items
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 5;

-- CASE: reate different outputs (usually in the SELECT statement). It is SQL’s way of handling if-then logic.
SELECT name,
 CASE
  WHEN genre = 'romance' THEN 'Chill'
  WHEN genre = 'comedy'  THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;