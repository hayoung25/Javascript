-- SQLite
CREATE TABLE awards (
   id INTEGER PRIMARY KEY,
   recipient TEXT NOT NULL,
   award_name TEXT DEFAULT 'Grammy'
);



-- 1. PRIMARY KEY columns can be used to uniquely identify the row. 
-- Attempts to insert a row with an identical value to a row already in the table will result in a constraint violation which will not allow you to insert the new row.

-- 2. UNIQUE columns have a different value for every row.
-- This is similar to PRIMARY KEY except a table can have many different UNIQUE columns.

-- 3. NOT NULL columns must have a value. 
-- Attempts to insert a row without a value for a NOT NULL column will result in a constraint violation and the new row will not be inserted.

-- 4. DEFAULT columns take an additional argument that will be the assumed value for an inserted row 
-- if the new row does not specify a value for that column.