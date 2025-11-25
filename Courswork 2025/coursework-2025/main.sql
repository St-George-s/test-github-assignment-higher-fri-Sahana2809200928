DESCRIBE ALL TABLES;


SELECT C.comicTitle, C.issue,P.publisherName,  C.valuation
FROM Comic C
JOIN Publisher P ON P.publisherID = C.publisherID
WHERE valuation > (
    SELECT AVG(valuation) + 300
    FROM Comic
)
;


SELECT CI.characterName, SUM(C.valuation)
FROM CharacterInfo CI
JOIN Comic C ON CC.comicID = C.comicID
JOIN ComicCharacter CC ON CC.characterID = CI.characterID
WHERE CI.characterName LIKE '%Duck%'  AND mainCharacter = 1
GROUP BY CC.characterID;

SELECT*
FROM Series;

SELECT*
FROM  ComicCharacter;

SELECT*
FROM CharacterInfo;

SELECT*
FROM Comic;

--comicTitle issue publisherName Double Price

SELECT C.comicTitle, C.issue, P.publisherName, SUM(C.valuation) * 2 AS 'Double price'
FROM Comic C
JOIN Publisher P ON P.publisherID = C.publisherID
JOIN Series S ON C.seriesID = S.seriesID
JOIN ComicCharacter CC ON CC.comicID = C.comicID
JOIN CharacterInfo CI ON CC.characterID = CI.characterID
WHERE S.seriesName = 'The OK Seven' AND CI.characterName LIKE 'Starlordly'
GROUP BY C.comicTitle;


-- SELECT comicTitle, issue, publisherName, valuation * 2 AS [Double
-- Price]
-- FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
-- WHERE Series.seriesName = "The OK Seven"
-- AND characterName = "Starlordly"

-- AND Comic.publisherID = Publisher.publisherID
-- AND Comic.seriesID = Series.seriesID
-- AND CharacterInfo.characterID = ComicCharacter.characterID
-- GROUP BY Comic.comicTitle;