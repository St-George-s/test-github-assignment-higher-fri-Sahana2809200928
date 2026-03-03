
--2c
SELECT C.forename, C.surname
FROM Customer C
JOIN Purchase P ON C.customerID = P.customerID
JOIN Movie M ON P.movieCode = M.movieCode
WHERE M.duration = (
    SELECT MIN(duration)
    FROM Movie
);

--2d
SELECT C.forename, C.surname, SUM(M.price) as 'Total spent(£)'
FROM Customer C
JOIN Purchase P ON C.customerID = P.customerID
JOIN Movie M ON P.movieCode = M.movieCode
JOIN Genre G ON G.genreID = M.genreID
WHERE G.genreName = 'Comedy'
GROUP BY C.customerID
ORDER BY SUM(M.price) DESC;

--2e
SELECT forename, surname, email
FROM customer, purchase, movie
WHERE customer.customerID = purchase.customerID 
AND Movie.movieCode = Purchase.movieCode
AND released >=1990 and released <2000
GROUP BY Customer.customerID
ORDER BY forename ASC; 
