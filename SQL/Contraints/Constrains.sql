-- NOT NULL CONSTRAINT
create table speakers (
  id integer NOT NULL, -- column which has not null 
  email varchar NOT NULL,
  name varchar NOT NULL,
  organization varchar,
  title varchar,
  years_in_role integer
);

INSERT INTO speakers (id, email, organization, title, years_in_role)
VALUES (1, 'awilson@ABCcorp.com', 'ABC Corp.', 'CTO', 6); -- This statement will not insert values instead incurring error because 'Name' is not defined in the statement