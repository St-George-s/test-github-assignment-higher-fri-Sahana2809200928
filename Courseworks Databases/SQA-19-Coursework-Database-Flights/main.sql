-- SELECT forename,surname, (B.adultTicket + B.childTicket + B.concessionTicket)  AS 'Total price'
-- FROM Booking B
-- JOIN Customer C ON C.customerID = B.customerID
-- WHERE C.customerID = 'GR01932'
-- GROUP BY C.customerID;



-- SELECT forename, surname
-- FROM Customer C
-- JOIN Booking B ON B.customerID = C.customerID
-- WHERE childTicket = (
--     SELECT MAX(childTicket)
--     FROM Booking
-- );


-- SELECT*
-- FROM Booking;

-- SELECT*
-- FROM Route;

-- SELECT *
-- FROM Flight;

-- SELECT*
-- FROM Customer;


SELECT C.forename, C.surname, (B.adultTicket * 5.50 +  B.childTicket * 2 + concessionTicket*1.50) AS 'Tax(£)'
FROM Booking B
JOIN Customer C ON C.customerID = B.customerID
WHERE C.customerID = 'GR01932'AND flightID = 'QH182';

SELECT C.forename, C.surname
FROM Customer C
JOIN Booking B ON C.customerID = B.customerID
WHERE B.childTicket = (
    SELECT MAX(childTicket)
    FROM Booking B
);

SELECT*
frOM Flight;