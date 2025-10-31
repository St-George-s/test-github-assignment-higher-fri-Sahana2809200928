-- DESCRIBE ALL TABLES;

SELECT * 
FROM Tracks 
WHERE duration_ms > 200000 and artist_ID = 1;

SELECT album_name
FROM Albums 
WHERE release_year > 2015 and release_year < 2018; 
-- having WHERE will result in only albums past 2018, although without all album names  

SELECT artist_ID
FROM Artists;

SELECT track_name
FROM Tracks;

SELECT album_name
FROM Albums
WHERE release_year < 2010;

SELECT artist_name
FROM Artists
WHERE artist_id < 10;













