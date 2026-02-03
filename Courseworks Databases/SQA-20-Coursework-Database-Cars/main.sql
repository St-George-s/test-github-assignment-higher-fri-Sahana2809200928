DESCRIBE ALL TABLES;
SELECT * FROM Job;
-- --PART A : 
-- --1a : 
-- --regNo, make, model, year, customerID
-- --1b :
-- --To count teh number of days that a car is in teh garage
-- --to update information concerning customers
-- --To display information on cars of customers by decending or acesning order

-- --PART B
-- --1b(i)






-- SELECT G.garageName, SUM(J.cost) AS 'Total sales'
-- FROM Garage G
-- JOIN Job J ON J.garageID = G.garageID
-- WHERE J.dateOut = '19-Jan-20'
-- GROUP BY G.garageID;

-- --1b(ii)

-- SELECT MAX(J.dateOut - J.dateIn) AS 'Number of days', J.regNo, G.garageName
-- FROM Job J
-- JOIN Garage G ON J.garageID = G.garageID;



SELECT Customer.customerID, forename, surname, AVG(cost) 
FROM Customer, Car, Job
WHERE Customer.customerID = Car.customerID AND car.regNo = Job.regNo
GROUP BY forename, surname, Customer.customerID
ORDER BY AVG(cost) DESC;
-- 





