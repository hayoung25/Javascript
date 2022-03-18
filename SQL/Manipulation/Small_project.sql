-- SQLite

-- Creating a table
CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

-- Inserting new values into table
INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends (id, name, birthday) 
VALUES (2, 'Mr. Park', '1993-01-23');
 
INSERT INTO friends (id, name, birthday) 
VALUES (3, 'Mr. Lin', '1995-02-12');

-- Updates tables values
UPDATE friends
SET name = 'Storm'
WHERE id = 1;

-- Altering table adding a new column
ALTER TABLE friends 
ADD COLUMN email TEXT; 

-- Update
UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

-- Delete a row 
DELETE FROM friends
WHERE id = 1;

