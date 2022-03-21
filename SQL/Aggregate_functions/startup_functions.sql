-- SQLite
SELECT * 
FROM startups;

SELECT COUNT(*)
FROM startups;

SELECT MAX(raised)
FROM startups

SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded)
FROM startups

SELECT category, AVG(valuation)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY 1
ORDER BY 2 DESC

SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3;

SELECT location, AVG(employees)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;