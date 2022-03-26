--  POSTGRESQL, pg_catalog.pg_roles —> a listing of all users in the database and understand what special permissions these users have.

SELECT rolname -- Select all role names in the table
FROM pg_catalog.pg_roles;

SET ROLE analyst; -- Setting a new role 

SELECT grantee, table_name, privilege_type 
FROM information_schema.table_privileges 
WHERE grantee = 'analyst';
-- Multiple selection of columns related to role


