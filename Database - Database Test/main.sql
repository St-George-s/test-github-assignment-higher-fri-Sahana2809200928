
--3.1
SELECT  E.episodeTitle  , S.showName, E.maxViewers, E.episodeDate
FROM Episode E
JOIN Show S ON E.showID = S.showID ;

--3.2
SELECT S.showName  AS 'Show', E.episodeTitle  as 'Episode'
FROM Show S
JOIN Episode E ON S.showID = E.showID
WHERE E.episodeDate LIKE '2024-12-%';

UPDATE Timeslot 
SET endTime  = '19:30'
WHERE showID = 2 AND airDate = '2024-12-24';


--PART C

SELECT S.showName, COUNT(ratingID)
FROM Show S
JOIN Episode E ON E.showID = S.showID
JOIN ViewerRating VR ON E.episodeID = VR.episodeID
GROUP BY S.showName
ORDER BY COUNT(ratingID) DESC;
