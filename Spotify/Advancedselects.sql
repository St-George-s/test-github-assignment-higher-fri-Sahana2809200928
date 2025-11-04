--    SELECT artist_name 
--    FROM Artists 
--    WHERE artist_name LIKE '--y%';

--    SELECT album_name, release_year 
--    FROM Albums 
--    WHERE release_year >= 2015 
--    ORDER BY release_year ASC;

-- SELECT a.album_name AS Album, a.release_year Year 
-- FROM Albums a 
-- WHERE a.release_year > 2010 
-- ORDER BY a.release_year;

-- SELECT artist_name, LENGTH(artist_name) AS Name_Length 
-- FROM Artists 
-- WHERE artist_name LIKE '_a%';

--T% refers to the starting letter allows to identify entities wthin a primary key staryt eith tha tletter
--order by assumes ascenfing order
--shorter name for Almbums, save time
--lenth of the artist name isntead of teh artist name by itself. 


-- SELECT artist_name
-- FROM Artists
-- WHERE artist_name LIKE 'S%e';

-- Select albums released after 2010, displaying the album name 
-- and a calculation of how many years ago they were released. 

SELECT *, 2025- release_year AS 'Years since release'
FROM Albums
WHERE release_year >2010;

--SELECT artist_name LENGTH(artist_name)
--FROM Artists
--WHERE LENGTH(artist_name) <= 5;
