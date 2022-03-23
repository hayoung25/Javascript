-- Creating new tables
CREATE TABLE book (
  title varchar(100),
  isbn varchar(50) PRIMARY KEY, -- Set as Primary key
  pages integer,
  price money,
  description varchar(256),
  publisher varchar(100)
);

CREATE TABLE chapter (
  id integer PRIMARY KEY, -- Set as Primary key
  number integer,
  title varchar(50),
  content varchar(1024)
);

CREATE TABLE author (
  name varchar(50),
  bio varchar(100),
  email varchar(20) PRIMARY KEY -- Set as Primary key
);

-- Insert Value
INSERT INTO book 
VALUES (
  'Postgres for Beginners',
  '0-5980-6249-1',
  25,
  4.99,
  'Learn Postgres the Easy Way',
  'Codecademy Publishing'
);

-- Information_schema
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage -- shows restrians in the table such as primary key and foreign keys
WHERE table_name = 'book';

-- Composite primary key
CREATE TABLE popular_books (
  book_title varchar(100),
  author_name varchar(50), 
  number_sold integer,
  number_previewed integer,
  PRIMARY KEY (book_title, author_name) -- It can designate multiple columns in a table to serve as the primary key,
);

-- Foreign Key 
CREATE TABLE book (
  title varchar(100),
  isbn varchar(50) PRIMARY KEY,
  pages integer,
  price money,
  description varchar(256),
  publisher varchar(100)
);

CREATE TABLE chapter (
  id integer PRIMARY KEY,
  book_isbn varchar(50) REFERENCES book(isbn), -- Seting foreign key
  number integer,
  title varchar(50),
  content varchar(1024)
);

SELECT * FROM book;
SELECT * FROM chapter;
SELECT book.title as book, chapter.title as chapters 
FROM book
JOIN chapter -- Join two tables with foreign key
ON book.isbn = chapter.book_isbn;
