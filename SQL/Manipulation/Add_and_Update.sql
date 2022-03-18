-- SQLite
ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT; 

UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4; 
 
SELECT * FROM celebs;