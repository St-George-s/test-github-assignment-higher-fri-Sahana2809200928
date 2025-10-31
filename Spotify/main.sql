DELETE FROM Tracks 
WHERE track_id = 5;

UPDATE Albums 
SET release_year = 2021 
WHERE album_id = 3;

UPDATE Artists 
SET artist_name = 'New Artist Name' 
WHERE artist_id IN (1, 2, 3);

INSERT INTO Tracks (track_id, track_name, artist_id, album_id, genre_id, duration_ms) 
VALUES (54, '2', 4, 4, 1, 180000), 
(55, 'Another Track', 5, 5, 2, 200000);
(20, 'hi', '2', '2', '2', '2000000')

INSERT INTO Genres (genre_id, genre_name) 
VALUES (21, 'Jazz');

DELETE FROM Artists 
WHERE artist_id BETWEEN 20 AND 25; 
-- ONLY IDS BETWEEN 2 VALUES

SELECT genre_name
FROM Genres;

DELETE FROM Albums
WHERE album_name = "Divide";

INSERT INTO Artist(artist_id , artist_name)
VALUES (100, 'HI');

DELETE FROM Tracks
WHERE duration_ms < 120000;

INSERT INTO Albums( album_id, album_name, release_year)
VALUES(3, 'HI', 'HI', 2009, )






