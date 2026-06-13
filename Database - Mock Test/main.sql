DESCRIBE ALL TABLES;

SELECT E.eventName AS 'Event Name', S.name AS 'shop Name', E.maxAttendees AS 'Max Atendees', E.eventDate AS 'Event date'
FROM Event E
JOIN Shop S ON S.shopID = E.shopID;



SELECT S.name AS 'shop Name', E.eventName AS 'event Name'
FROM Shop S
JOIN Event E on S.shopID = E.eventID
WHERE eventDate = '2024-12-25';



SELECT S.name, COUNT(B.bookingID)
FROM Shop S
JOIN Booking B ON B.eventID = E.eventID
JOIN Event E ON E.shopID = S.shopID
GROUP BY S.shopID
ORDER BY name;


#A functional requirement was to identify the dates on which different events but my database can only fins events on  25th December 

SELECT*
FROM Show;

SELECT*
FROM ViewerRating;

SELECT*
FROM Episode;

SELECT*
FROM Timeslot;