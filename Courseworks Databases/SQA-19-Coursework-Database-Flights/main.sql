SELECT forename,surname, (B.adultTicket + B.childTicket + B.concessionTicket)  AS 'Total price'
FROM Booking B
JOIN Customer C ON C.customerID = B.customerID
WHERE C.customerID = 'GR01932'
GROUP BY C.customerID;



SELECT forename, surname
FROM Customer C
JOIN Booking B ON B.customerID = C.customerID
WHERE childTicket = (
    SELECT MAX(childTicket)
    FROM Booking
);


SELECT*
FROM Booking;

SELECT*
FROM Route;

SELECT *
FROM Flight;

SELECT*
FROM Customer;
