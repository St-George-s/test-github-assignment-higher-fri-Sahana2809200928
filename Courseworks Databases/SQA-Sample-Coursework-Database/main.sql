DESCRIBE ALL TABLES;



SELECT C.firstName, C.surname, CO.voucherID, SUM(CO.quantityPurchased * V.price) AS "Amount of money spent on voucher £"
FROM CustomerOrder CO     
JOIN Voucher V ON CO.voucherID = V.voucherID
JOIN Customer C ON C.custID = CO.custID
WHERE V.category = "Adventure" AND voucherName LIKE '%escape room%'
GROUP BY C.custID
ORDER BY CO.voucherID ;



SELECT V.voucherID, S.supplierName, V.voucherName, (V.quantityAvailable - SUM(CO.quantityPurchased)) AS 'AVAILABLE'
FROM Voucher V
JOIN Supplier S ON S.supplierCode = V.supplierCode
JOIN CustomerOrder CO ON CO.voucherID = V.voucherID
WHERE V.voucherID = 'V543';

SELECT S.supplierName, V.voucherName, V.price, COUNT(CO.custID) AS 'Number of customers'
FROM Voucher V
JOIN Supplier S On S.supplierCode = V.supplierCode
JOIN CustomerOrder CO ON CO.voucherID = V.voucherID
WHERE price < 15 AND category = 'Family'
GROUP BY V.voucherName 
ORDER BY  COUNT(CO.custID) DESC;


-- Blanks can be left, leading to gaps in a specific instance, must use a prescence check
-- Incorrect data types being entered into a column field, which results in invalid data - use a type check
-- expiry date if voucher may have past
-- quantity availbel must be 0 or greater - different number may be entered  
