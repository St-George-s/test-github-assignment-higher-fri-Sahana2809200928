USE project1;

DROP TABLE IF EXISTS Swimmers;

CREATE TABLE Swimmers (
  swimmer_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name  VARCHAR(50) NOT NULL,
  squad      VARCHAR(50) NOT NULL,
  stroke_pref VARCHAR(20) NULL,
  personal_best_50_free_seconds DECIMAL(5,2) NULL
);

INSERT INTO Swimmers 
(first_name, last_name, squad, stroke_pref, personal_best_50_free_seconds)
VALUES
('Erin',  'Smith', 'Lane 1', 'Freestyle', 33.20),
('Chloe', 'Jones', 'Lane 5', 'Breaststroke', 41.75),
('Alba',  'Brown', 'Lane 1', 'Backstroke', 34.10);
