DESCRIBE ALL TABLES;

SELECT*
FROM Walker
LIMIT 2;

SELECT*
FROM Planner
LIMIT 2;

SELECT*
FROM Route
LIMIT 2;

SELECT*
FROM Walk
LIMIT 2;


SELECT P.forename, P.surname, P.plannerNo, count(W.WalkID)
FROM Planner P
JOIN Route R ON P.plannerNo = R.plannerNo
JOIN Walk W ON W.routeID = R.routeID
GROUP BY P.plannerNo
ORDER BY count(W.WalkID) DESC;