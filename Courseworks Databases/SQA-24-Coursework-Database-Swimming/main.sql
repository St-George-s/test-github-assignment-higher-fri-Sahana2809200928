



-- --q 2c
-- SELECT S.initial, S.surname, S.swimCategory, T.teamName, count(R.raceNumber) AS 'Races won'
-- FROM Swimmer S 
-- JOIN Result R on S.swimmerID = R.swimmerID
-- JOIN Team T on T.teamRef = S.teamRef
-- WHERE R.position = 1
-- GROUP BY S.swimmerID
-- ORDER BY S.initial;
-- GROUP BY S.swimmerID
-- ORDER BY min(R.racetime)
-- LIMIT 1;

-- --what if position was in a table with no foreign key, 
-- --CAN U ONLY ADD ONE TABLE ONTO THE 
-- --SWAM IN LANES 1 OR 8 WITH THE FASTEST TIME FROM ANY RACE

-- --q2d
-- SELECT S.initial, S.surname, T.teamName, E.city, E.eventDate
-- FROM Swimmer S
-- JOIN Result Re ON S.swimmerID = Re.swimmerID
-- JOIN Team T ON T.teamRef = S.teamRef
-- JOIN Race Ra ON Ra.raceNumber= Re.raceNumber
-- JOIN Event E ON E.eventID = Ra.eventID
-- WHERE Re.raceTime = (
--     SELECT MIN(raceTime)
--     FROM Result
--     WHERE lane = 1 or lane =8
-- ) 
-- LIMIT 1;







-- SELECT T.teamName, COUNT(R.position) AS 'TOTAL MEDALS WON'
-- FROM  Swimmer S
-- JOIN Team T ON S.teamRef = T.teamRef
-- JOIN Result R on R.swimmerID = S.swimmerID
-- WHERE R.position = 1 or  R.position = 2 or  R.position = 3
-- GROUP BY T.teamName
-- ORDER BY COUNT(R.position) DESC;

SELECT S.initial, S.surname, S.swimCategory, T.teamName, COUNT(R.position) AS 'Races won'
FROM Result R 
JOIN Swimmer S ON S.swimmerID = R.swimmerID
JOIN Team T ON  S.teamRef = T.teamRef
WHERE position = '1'
GROUP BY  S.swimmerID
ORDER BY initial;

SELECT S.initial, S.surname, T.teamName, E.city, E.eventDate
FROM Swimmer S
JOIN Event E ON  E.eventID = Ra. eventID 
JOIN Race Ra ON  Ra.raceNumber = Re.raceNumber
JOIN Result Re ON Re.swimmerID = S.swimmerID
JOIN Team T ON  S.teamRef = T.teamRef
WHERE lane = 1 OR lane = 8
ORDER BY raceTime ASC
LIMIT 1;

SELECT T.teamName, COUNT(position) AS 'TOTAL MEDALS WON'
FROM Swimmer S
JOIN Result Re ON Re.swimmerID = S.swimmerID
JOIN Team T ON  S.teamRef = T.teamRef
WHERE position = 1 OR position = 2  OR position = 3
GROUP BY T.teamName
ORDER BY COUNT(Re.position) DESC;








