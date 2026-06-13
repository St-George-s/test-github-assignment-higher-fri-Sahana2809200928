-- DESCRIBE ALL TABLES;
-- --QUSITONTS 2B

-- -- SELECT G.gnomeName, SUM(GP.quantity) AS 'TOTAL GNOMES SOLD'
-- -- FROM Gnome G
-- -- JOIN GnomePurchase GP ON GP.gnomeID = G.gnomeID
-- -- WHERE g.description LIKE '%solar%' 
-- -- GROUP BY G.gnomeName
-- -- ORDER BY sum(GP.quantity) DESC;

-- -- SELECT*
-- -- FROM CustomerOrder;
    
-- --QUESTION 2C

-- -- SELECT MAX(unitprice)
-- -- FROM Gnome;

-- -- SELECT C.emailAddress, GP.orderID, GP.quantity
-- -- FROM GnomePurchase GP
-- -- JOIN Customer C ON C.customerID = O.customerID
-- -- JOIN Orders O ON O.orderID = GP.orderID
-- -- JOIN Gnome G ON G.gnomeID = GP.gnomeID
-- -- WHERE GP.quantity >= 3 AND G.unitPrice = (
-- --     SELECT MAX(unitPrice)
-- --     FROM Gnome
-- -- );

-- -- SELECT C.forename, C.surname, ROUND(SUM(GP.Quantity * 1.2 * G.unitPrice ),2) AS 'total to pay(£)'
-- -- FROM Customer C
-- -- JOIN Orders O ON C.customerID = O.customerID
-- -- JOIN GnomePurchase GP ON O.orderID = GP.orderID
-- -- JOIN Gnome G ON G.gnomeID = GP.gnomeID
-- -- WHERE O.orderID = 'ord0024'JHHGVHGVHGV;



-- -- SELECT *
-- -- FROM GnomePurchase;


-- -- JOIN Gnome G ON G.gnomeID = GP.gnomeID
-- -- WHERE O.orderID = 'ord0024'
-- -- GROUP BY O.orderID;

-- DESCRIBE ALL TABLES;

-- SELECT *
-- FROM Customer;

-- SELECT *
-- FROM Gnome;

-- SELECT *
-- FROM Orders;

-- SELECT *
-- FROM GnomePurchase;



SELECT G. gnomeName, SUM(quantity) AS 'Total gnomes sold' 
FROM GnomePurchase GP
JOIN Gnome G ON GP.gnomeID = G.gnomeID
WHERE G.description LIKE '%solar%'
GROUP BY G.gnomeID
ORDER BY SUM(quantity) DESC;



SELECT C.emailAddress, GP.orderID, GP.quantity
FROM GnomePurchase GP
JOIN Orders O ON O.orderID = GP.orderID
JOIN Customer C ON C.customerID =O.customerID
JOIN Gnome G ON GP.gnomeID = G.gnomeID
WHERE  quantity > 3 AND G.unitPrice = (
    SELECT MAX(unitPrice)
    FROM Gnome
)
GROUP by GP.gnomePurchaseID;

-- SELECT forename, surname, (quantity * 1.2) AS 'total to pay £'
-- FROM Customer C
-- JOIN Orders O ON C.customerID = O.customerID
-- JOIN GnomePurchase GP ON GP.orderID = O.orderID
-- JOIN gnome G ON GP.gnomeID - G.gnomeID
-- WHERE O.orderID = 'ord0024' ;

SELECT forename, surname, ROUND(SUM(quantity * unitPrice * 1.2),2 )AS [Total to Pay £]
FROM Customer, Gnome, GnomePurchase, Orders
WHERE Orders.orderID="ord0024"
AND Customer.customerID=Orders.customerID
AND Orders.orderID=GnomePurchase.orderID
AND Gnome.gnomeID=GnomePurchase.gnomeID; 
