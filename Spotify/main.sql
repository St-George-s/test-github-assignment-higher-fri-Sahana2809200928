SELECT * 
FROM Tracks 
WHERE album_id IN (
  SELECT album_id 
  FROM Albums 
  WHERE release_year > 2018
 );




