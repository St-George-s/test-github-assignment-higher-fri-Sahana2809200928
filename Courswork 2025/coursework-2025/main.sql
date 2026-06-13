-- DESCRIBE ALL TABLES;

SELECT C.comicTitle, C.issue, P.publisherName, C.valuation
FROM Comic C
JOIN Publisher P ON C.publisherID = C.publisherID
WHERE C.valuation >= (
    SELECT AVG(valuation) + 300
    FROM Comic C
)
GROUP BY C.comicTitle;

SELECT CI.characterName , SUM(C.valuation) AS 'Total valuation'
FROM ComicCharacter CC 
JOIN Comic C ON C.comicID = CC.comicID
JOIN characterInfo CI ON CI.characterID = CC.characterID
WHERE CC.mainCharacter = 1 AND CI.characterName LIKE '%Duck%'
GROUP BY characterName 
ORDER BY SUM(C.valuation) DESC ;


SELECT comicTitle, issue, publisherName, valuation * 2 AS [Double
Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"
AND characterName = "Starlordly"
AND Comic.publisherID = Publisher.publisherID
AND Comic.seriesID = Series.seriesID
AND CharacterInfo.characterID = ComicCharacter.characterID
AND Comic.comicID = ComicCharacter.comicID
GROUP BY comicTitle;


















-- SELECT C.comicTitle, C.issue, P.publisherName, C.valuation
-- FROM Comic C
-- JOIN Publisher P ON C.publisherID = P.publisherID
-- WHERE C.valuation >= (
--     SELECT AVG(valuation) + 300
--     FROM Comic
-- );


-- SELECT CI.characterName, SUM(C.valuation) AS 'Total valuation'
-- FROM ComicCharacter CC
-- JOIN Comic C ON CC.comicID = C.comicID
-- JOIN CharacterInfo CI ON CI.characterID = CC.characterID
-- WHERE CC.mainCharacter = 1 AND CI.characterName LIKE '%Duck%'
-- GROUP BY  CC.characterID
-- ORDER BY SUM(C.valuation) DESC ;


-- SELECT C.comicTitle, C.issue, P.publisherName, SUM(C.valuation) * 2 AS 'double price'
-- FROM Comic C
-- JOIN Publisher P ON C.publisherID = P.pubclisherID
-- JOIN ComicCharacter CC ON C.comicID = CC.comicID
-- JOIN CharacterInfo CI ON CI.characterID = CC.characterID
-- JOIN Comic C ON C.seriesID = S.seriesID
-- WHERE CI.characterName = 'Starlordly' AND seriesName = 'The OK Seven';

-- SELECT comicTitle, issue, publisherName, valuation *2 AS [Double
-- Price]
-- FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
-- WHERE Series.seriesName = "The OK Seven"
-- AND characterName = "Starlordly"
-- AND Comic.publisherID = Publisher.publisherID
-- AND Comic.seriesID = Series.seriesID
-- AND CharacterInfo.characterID = ComicCharacter.characterID
-- AND ComicCharacter.comicID = Comic.comicID
-- GROUP BY comicTitle;