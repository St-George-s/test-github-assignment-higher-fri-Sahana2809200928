--2C

SELECT S.initial, S.surname, S.swimCategory, T.teamName, SUM(Re.position) AS 'Total races won'
FROM Swimmer S
JOIN Result Re ON S.swimmerID = Re.swimmerID
JOIN Team T ON T.teamRef = S.teamRef
WHERE position = 1
GROUP BY S.swimmerID
ORDER BY S.initial;

--2D

SELECT S.initial, S.surname, T.teamName, E.city, E.eventDate
FROM Swimmer S
JOIN Team T ON T.teamRef= S.teamRef
JOIN Result Re ON Re.swimmerID = S.swimmerID
JOIN Race Ra ON Ra.raceNumber = Re.raceNumber
JOIN Event E ON E.eventID = Ra.eventID
WHERE Re.lane = 1 or Re.lane = 8 AND  E.eventDate = '06/01/2024'
ORDER BY Re.raceTime ASC
LIMIT 1;


--2e
SELECT teamName, COUNT(position) AS [Total medals won]
FROM Result, Swimmer, Team
WHERE Result.swimmerID = Swimmer.swimmerID AND Swimmer.teamRef =
Team.teamRef AND (position = 1 or position = 2 or position = 3)
GROUP BY teamName
ORDER BY [Total medals won]  DESC;



