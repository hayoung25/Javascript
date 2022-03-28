--CREATE TRIGGER

-- Creating a trigger with trigger name'insert_trigger'
CREATE TRIGGER insert_trigger 
-- Trigger is attached to 'customers' table and it will be activated before anything will be inserted into the 'customers' table
  BEFORE INSERT ON customers 
-- For every row
  FOR EACH ROW 
-- What is trigger will be the insert_function()
  EXECUTE PROCEDURE insert_function() 


-- BEFORE, AFTER
CREATE TRIGGER after_trigger
-- After attribute allows to change or trigger a function after the given condition is finished
AFTER UPDATE ON customers
FOR EACH ROW
EXECUTE PROCEDURE log_customers_change();


--FOR EACH ROW vs STATEMENT
CREATE TRIGGER each_statement_trigger
AFTER UPDATE ON customers
-- For each row is activated for each row, but for each statement is only activated when a query statement is activated
FOR EACH STATEMENT
EXECUTE PROCEDURE statement_function();


--WHEN ATTRIBUTE
CREATE TRIGGER update_trigger_high
BEFORE UPDATE ON clients
FOR EACH ROW 
-- trigger is activated only when the new data's total_spent value is greater than 1000
WHEN (NEW.total_spent >= 1000)
EXECUTE PROCEDURE set_high_spender();


-- CHECKING TRIGGERS
SELECT * FROM information_schema.triggers; -- shows triggers attached to tables


-- DELETE TRIGGERS
DROP TRIGGER im_a_bad_trigger ON orders -- delete a trigger name 'im_a_bad_trigger' from table 'orders'