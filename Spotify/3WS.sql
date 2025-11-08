--    SELECT artist_name 
--    FROM Artists 
--    WHERE artist_name LIKE 'T%';

  

-- SELECT album_name, release_year 
-- FROM Albums 
-- WHERE release_year >= 2015 
-- ORDER BY release_year ASC;

-- SELECT a.album_name AS Album, a.release_year  
-- FROM Albums a 
-- WHERE a.release_year > 2010 
-- ORDER BY a.release_year;

-- SELECT artist_name, LENGTH(artist_name) AS Name_Length 
-- FROM Artists 
-- WHERE artist_name LIKE '_a%';


-- SELECT artist_name
-- FROM Artists
-- WHERE artist_name LIKE 'S%e';

-- SELECT a.album_name AS 'album name', 2025-(a.release_year) AS 'years since release'
-- FROM Albums a
-- WHERE a.release_year > 2010;

-- SELECT artist_name, LENGTH(artist_name) as 'Name Legnth'
-- FROM Artists
-- WHERE LENGTH(artist_name > 5);
