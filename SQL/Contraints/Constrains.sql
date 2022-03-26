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


-- ALTERING CONSTRAINTS
ALTER TABLE speakers
ALTER COLUMN name SET NOT NULL; -- Alter column contraint adding not null contraint

UPDATE speakers
SET organization = '' -- Changing value to a placeholder where it's value is NULL
WHERE organization IS NULL;

-- Set contstraint not null on the organization column
ALTER TABLE speakers
ALTER COLUMN organization SET NOT NULL;


-- CHECK STATEMENT
ALTER TABLE speakers
ADD CHECK (years_in_role < 100) -- Adding check restraint on years_in_role column

ALTER TABLE speakers
ADD CHECK (years_in_role < 100 AND years_in_role > 0);
-- Adding check which can check two conditions with syntax AND

ALTER TABLE attendees
ADD CHECK (standard_tickets_reserved + vip_tickets_reserved = total_tickets_reserved);
-- Check contraint with other conditions


--UNIQUE CONSTRAINT
ALTER TABLE speakers
ADD UNIQUE (email); -- Adding Unique contraint on email column which means each row must have different email value

CREATE TABLE registrations (
    id integer NOT NULL,
    attendee_id integer NOT NULL,
    session_timeslot timestamp NOT NULL,
    talk_id  integer NOT NULL,
    UNIQUE (session_timeslot, attendee_id) -- Add Unique contraint on both comlumns which restricts to not have same combination of both column but each column can have duplicated value of rows.
);

-- PRIMARY KEY (UNIQUE and NOT NULL)
ALTER TABLE speakers
ADD PRIMARY KEY (id);

INSERT INTO speakers (email, name, organization, title, years_in_role)
VALUES ('J.Saunders@ABCTech.com', 'Joan Saunders', 'ABC Tech.',  'Sr. Data Scientist', 6);
-- This would incur error because the insert has no value of ID number

INSERT INTO speakers (id, email, name, organization, title, years_in_role)
VALUES (1, 'J.Saunders@ABCTech.com', 'Joan Saunders', 'ABC Tech.',  'Sr. Data Scientist', 6);
-- This will be proceeded because it is adding value with id column


-- FOREIGN KEY
ALTER TABLE talks
ADD FOREIGN KEY (speaker_id) --Forign key(a new column attaching to talk table)'s column name
REFERENCES speakers (id); -- foreign key referring to id in speakers table

INSERT INTO talks (id, title, speaker_id, estimated_length, session_timeslot) VALUES (21, 'Data Warehousing Best Practices', 101, 30, '2020-08-15 18:00');
-- when it comes to insert value into table, if the foreign key does not exist, it causes error

-- CASCADE ON FOREIGN KEY
ALTER TABLE talks
ADD FOREIGN KEY (speaker_id)
REFERENCES speakers (id) ON DELETE CASCADE; -- Attaching delete casecade attribute on foreign key.

DELETE FROM speakers where id = 2;
-- This statement will execute to delete all the rows in talks table of which foreign key is 'id = 2'