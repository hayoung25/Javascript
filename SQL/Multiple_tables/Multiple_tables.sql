-- COMBINE TABLES
SELECT *
FROM orders
JOIN subscriptions
	ON orders.subscription_id = subscriptions.subscription_id
WHERE subscriptions.description = 'Fashion Magazine';

-- INNER JOIN: it only joins existing matches
SELECT COUNT(*)
FROM newspaper; -- returns 60

SELECT COUNT(*)
FROM online; -- returns 65

SELECT COUNT(*)
FROM newspaper
JOIN online
	ON newspaper.id = online.id; -- returns 50

-- LEFT JOIN: it joins tables according to the left table. When id is not matched, left table contents remains with null values on right table columns

SELECT count(*)
FROM newspaper
LEFT JOIN online
	ON newspaper.id = online.id
WHERE online.id IS NULL; -- returns 10

-- PRIMARY KEY
-- Primary keys have a few requirements:
-- None of the values can be NULL.
-- Each value must be unique (i.e., you can’t have two customers with the same customer_id in the customers table).
-- A table can not have more than one primary key column.

-- CROSS JOIN: Combinations
SELECT COUNT(*)
FROM newspaper -- count: 60
CROSS JOIN months; -- count: 12
--returns count: 60 * 12 = 720

-- UNION: Unite tables
SELECT * 
FROM newspaper 
UNION 
SELECT * 
FROM online;

-- WITH: using multiple queries

-- Creating previous_query
WITH previous_query AS (
   SELECT customer_id,
      COUNT(subscription_id) AS 'subscriptions'
   FROM orders
   GROUP BY customer_id
)

SELECT customers.customer_name, 
   previous_query.subscriptions -- Use previous_query and join it to customers table
FROM previous_query
JOIN customers
  ON previous_query.customer_id = customers.customer_id;