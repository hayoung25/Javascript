-- SIZE CHECKING STATEMENTS
-- 'pg_total_relation_size' will return the size of the table and all its indexes in bytes. These values are often in the millions or billions and thus hard to read.

-- 'pg_table_size' and 'pg_indexes_size' return the size of the table’s data and table’s indexes in bytes. The sum of these two functions is equal to 'pg_total_relation_size'

-- 'pg_size_pretty' can be used with the functions above to format a number in bytes as KB, MB, or GB.


-- UPDATE & DELETE 
-- update and delete do take storage in the hardware.

-- PostgreSQL doesn’t physically delete the content from the disk. Instead, the database engine marks those rows so that they aren’t returned in user queries. These rows are called dead tuples, and although they aren’t referenced in the current version of databases’ tables, they still occupy space on disk and can affect performance.

--The behavior for DELETE operations is slightly different. Unlike updates, deletes don’t add space to a table. However, a DELETE statement will create dead tuples and leave the size of the table unchanged.

-- VACUUM
-- vacuum can be used to manage storage space.

-- Running VACUUM <table name>; will vacuum a specific table, while a VACUUM statement without a table name will run on the entire database.

--you may not see much of a decrease in space before and after a vacuum. This is because a plain VACUUM will only clear tables’ dead tuples where possible. Depending on which rows in your table are updated, this can clear anywhere between 0 and 100% of dead tuples.

--If VACUUM cannot clear the dead tuples, PostgreSQL will mark the space occupied by dead tuples for reuse when new data is inserted into the table. 
-- Syntax = VACUUM '<table_name>'


-- AUTOVACUUM
--When using autovacuum, PostgreSQL periodically checks for tables that have had a large number of inserted, updated or deleted tuples that could be vacuumed to improve performance.

--When autovacuum is enabled and finds such a table,  VACUUM ANALYZE command is run. This statement is a combination of two separate operations.

-- VACUUM, which manages the dead tuples in a database table

--ANALYZE, which is a statement that allows PostgreSQL look at a table and gather information about contents. PostgreSQL then stores this data internally and uses it to ensure that queries are planned in the most efficient way given the structure of the table.

--pg_stat_all_tables is table that contains internal PostgreSQL statistics; you can query for a specific table’s statistics by filtering on the column relname
SELECT relname, 
    last_vacuum,
    last_autovacuum, 
    last_analyze
FROM pg_stat_all_tables 
WHERE relname = 'books'; -- checks last time for each command


-- VACUUM FULL 
--There is an alternative VACUUM method, VACUUM FULL which rewrites all the data from a table into a “new” location on disk and only copies the required data (excluding dead tuples). 

-- One of the significant drawbacks from VACUUM FULL is that it’s a slow operation that blocks other operations on the table while it’s working. 

-- Although a plain VACUUM won’t reduce table size, plain VACUUM is designed to be able to run in parallel with normal reading and writing of the table. 
VACUUM FULL <table name>


-- TRUNCATE
-- TRUNCATE quickly removes all rows from a table. 

-- unqualified delete — a DELETE that affects all rows (e.g. DELETE * FROM table WHERE true;)

-- PostgreSQL doesn’t scan through the table first, TRUNCATE runs much faster on large tables. Finally, TRUNCATE simultaneously reclaims disk space immediately, rather than requiring a subsequent VACUUM or VACCUM FULL operation.
TRUNCATE mock.current_day_logins;
