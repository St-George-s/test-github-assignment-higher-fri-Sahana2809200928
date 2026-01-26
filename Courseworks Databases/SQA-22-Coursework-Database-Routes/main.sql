DESCRIBE ALL TABLES;

-- SELECT*
-- FROM Walker
-- LIMIT 2;

-- SELECT*
-- FROM Planner
-- LIMIT 2;

-- SELECT*
-- FROM Route
-- LIMIT 2;

-- SELECT*
-- FROM Walk
-- LIMIT 2;

-- --2B
-- SELECT P.forename, P.surname, P.plannerNo, count(W.WalkID)
-- FROM Planner P
-- JOIN Route R ON P.plannerNo = R.plannerNo
-- JOIN Walk W ON W.routeID = R.routeID
-- GROUP BY P.plannerNo
-- ORDER BY count(W.WalkID) DESC;

-- --2C
-- SELECT Wal.walkerNo, Wal.forename, Wal.surname, Wal.telNo
-- FROM Walker Wal
-- JOIN Walk Wa ON Wa.walkerNo = Wal.walkerNo
-- JOIN Route R ON R.routeID = Wa.routeID
-- WHERE R.distance = (
--     SELECT MAX(Distance)
--     FROM Route
-- )
-- GROUP BY Wa.walkerNo;

-- SELECT R.routeID, woodName, description
-- FROM Route R

-- ]
-- WHERE R.footwear LIKE '%shoe%';



-- SELECT P.forename, P.surname, P.plannerNo, COUNT(W.routeID)
-- FROM Planner P
-- JOIN Walk W ON R.routeID = W.routeID
-- JOIN Route R ON R.plannerNo = P.plannerNo
-- GROUP BY P.plannerNo
-- ORDER BY COUNT(W.routeID) DESC;




-- SELECT WA.walkerNo, WA.forename, WA.surname, WA.telNo
-- FROM Walker WA
-- JOIN Walk W ON WA.walkerNo = W.walkerNo
-- JOIN Route R ON R.routeID = W.routeID
-- WHERE R.Distance = (
--     SELECT MAX(distance)
--     FROM Route
-- )
-- GROUP BY WA.walkerNo;



-- SELECT routeID, woodName, description
-- FROM Route
-- WHERE footwear LIKE '%shoes%';


DESCRIBE ALL TABLES;

SELECT*
FROM Walker

SELECT*
FROM Route

SELECT*
FROM Walk

SELECT*
FROM Planner