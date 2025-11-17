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

   -- SELECT artist_name 
   -- FROM Artists  
   -- WHERE artist_name LIKE '__y%';

   SELECT *
   FROM Albums;

   -- SELECT a.album_name album , a.release_year Year 
   -- FROM Albums a
   -- WHERE a.release_year > 2010 
   -- ORDER BY a.release_year;

   SELECT A.album_name name, release_year Year
   FROM Albums a
   WHERE album_name IN ('25', 'Divide');

   --  - Write a query to select track names that start with 'S' and end with 'e'.
   -- - Select albums released after 2010, displaying the album name and a calculation of how many years ago they were released.
   -- - Write a query to display artist names with their name lengths, only for artists whose names are longer than 5 characters.

SELECT*
FROM Tracks T
WHERE T.track_name LIKE 'S%e';

SELECT album_name, 2025 - release_year AS 'years ago released'
FROM Albums A
WHERE A.release_year >2010;


SELECT a.artist_name, LENGTH(a.artist_name) AS 'name lenghts'
FROM Artists a
WHERE LENGTH(a.artist_name) >5;

