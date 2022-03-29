-- CREATE INDEX
CREATE INDEX customers_city_idx ON customers (city);
-- creates index named 'customers_city_idx' on city column in customers table
SELECT *
FROM pg_Indexes
WHERE tablename = 'customers'; -- statement for checking index 


-- MULTI-COLUMN INDEX
CREATE INDEX customers_last_name_first_name_idx ON customers (last_name, first_name);
--creating multicolum index


--DROP INDEX
DROP INDEX customers_last_name_idx;
-- removing index from the table


-- WHY NOT INDEX ALL?
-- Everything has a cost. Indexes speed up searching and filtering, however, they slow down insert, update, and delete statements. It also takes storage