-- PARTIAL INDEX
-- creating index in subset of a table
CREATE INDEX customers_years_old_teen_idx ON customers (years_old)
WHERE years_old BETWEEN 13 AND 19;
--creating partial index


-- ORDER BY
CREATE INDEX customers_state_name_email_address_ordered_idx ON customers(state_name DESC, email_address ASC);
-- creating multi-column index, ordering by desc on state_name column and asc on email_address column


-- PRIMARY KEY
-- primary key is by default indexed column


-- CLUSTERED INDEX 
    -- organize actual Data using index
    -- has only one (cannot use more than one index because they conflicts)
CLUSTER customers USING customers_last_name_idx;
-- cluster customers table using index on last_name in the table


-- NON-CLUSTERED INDEX
  -- index referencing to actual data
  -- can have multiple non-clustered index


  -- INDEXES BASED ON EXPRESSIONS
CREATE UNIQUE INDEX customers_email_address_lower_unique_idx ON customers(LOWER(email_address)); -- making 'unique' index which constraints duplicate of email_address

INSERT INTO customers (first_name, last_name, email_address)
VALUES ('John', 'Doe', 'ExaMPle@SampLE.COM'),
('Jane','Doe','example@sample.com');
-- this statement will be rejected becaause the email address is same