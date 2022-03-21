-- -- Counting total items
-- SELECT COUNT(*) 
-- FROM fake_apps;

-- SELECT COUNT(*) 
-- FROM fake_apps
-- WHERE price = 0;

-- -- Sum values
-- SELECT SUM(downloads)
-- FROM fake_apps;

-- -- Max, Min 
-- SELECT MIN(downloads)
-- FROM fake_apps;

-- SELECT MAX(price)
-- FROM fake_apps;

-- -- Average
-- SELECT AVG(downloads)
-- FROM fake_apps;
 
-- SELECT AVG(price)
-- FROM fake_apps;
 
--  --Round
-- SELECT name, ROUND(price, 0)
-- FROM fake_apps;

-- SELECT ROUND(AVG(price), 2)
-- FROM fake_apps;

-- -- Group by
-- SELECT price, COUNT(*) 
-- FROM fake_apps
-- GROUP BY price;

-- SELECT price, COUNT(*) 
-- FROM fake_apps
-- WHERE downloads > 20000
-- GROUP BY price;

-- SELECT category, SUM(downloads)
-- FROM fake_apps
-- GROUP BY category;

-- SELECT category, price, AVG(downloads)
-- FROM fake_apps
-- GROUP BY category, price;

-- -- Having
-- SELECT price, ROUND(AVG(downloads)), COUNT(*)
-- FROM fake_apps
-- GROUP BY price
-- HAVING COUNT(*) > 10;