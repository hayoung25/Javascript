--  POSTGRESQL, pg_catalog.pg_roles —> a listing of all users in the database and understand what special permissions these users have.
SELECT rolname -- Select all role names in the table
FROM pg_catalog.pg_roles;

SET ROLE analyst; -- Setting a new role to analyst 

SELECT grantee, table_name, privilege_type 
FROM information_schema.table_privileges 
WHERE grantee = 'analyst';
-- Multiple selection of columns related to role


-- CREATE ROLE
CREATE ROLE analyst WITH LOGIN NOSUPERUSER; 

CREATE ROLE analyst_mgmt WITH CREATEROLE LOGIN NOSUPERUSER; -- Assign multiple roles

ALTER ROLE analyst_mgmt WITH CREATEDB; -- Add CreateDB role to analyst_mgmt


-- MODIFY ROLES (giving authority to user to modify DB schema)
GRANT USAGE, CREATE ON SCHEMA marketing TO analyst;
-- giving Usage of marketing schema to analyst

GRANT SELECT, INSERT, DELETE ON marketing.prospects TO analyst; -- Granting modification authorities to analyst

REVOKE DELETE ON marketing.prospects FROM analyst;
-- Take back DELETE from analyst

SET ROLE analyst;
 
DELETE FROM marketing.prospects WHERE id = 2;
-- this query is not working because analyst have no authority to use DELETE for this DB schema


-- MODIFYING DEFAULT PERMISSIONS
GRANT SELECT, DELETE, UPDATE, INSERT ON census.economic_survey TO writer; -- Granting permssions to a role called 'writer' in economic_survey table from census schema

ALTER DEFAULT PRIVILEGES 
IN SCHEMA census
GRANT SELECT, DELETE, UPDATE, INSERT ON TABLES TO writer; 
-- changing privileges in schema census giving permissions to write role for all tables in census schema


--GROUPS
CREATE ROLE pgdba WITH SUPERUSER CREATEDB NOLOGIN;
-- creating pgdba role which has permission of superuser, createDB, and nologin

CREATE ROLE david WITH LOGIN IN ROLE employees, pgdba;
-- create user role 'david' with Login permission, in role groups of employees and pgdba

SELECT rolname, rolsuper
FROM pg_catalog.pg_roles 
WHERE rolname = 'david';
-- checking the name, rolesuper of david role


-- COLUMN LEVEL SECURITY
GRANT SELECT ON projects TO manager;
--granting select permission in project table to manager role

GRANT UPDATE (project_name, project_status) ON projects to manager;
-- granting update permission to manager role with restriction that only allows to update project_name, project_status column in projects table

select * 
from information_schema.column_privileges
where grantee = 'manager';
-- this statement shows all of manager role's permissions. 


-- ROW LEVEL SECURITY (POLICY)
CREATE POLICY sales_rls_policy ON accounts FOR DELETE
TO sales USING (salesperson = current_user);
-- creating a policy named' sales_rls_policy' on table 'accounts' as to 'sales' role's 'Delete' permission. it only allows to use delete when the condition is met

ALTER TABLE accounts ENABLE ROW LEVEL SECURITY;
-- apply the policy to the table 'accounts'