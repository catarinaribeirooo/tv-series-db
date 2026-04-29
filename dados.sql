LOAD DATA INFILE '/var/lib/mysql-files/series.csv'
INTO TABLE SERIES
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(SeriesId,Title,Rate, Premiere, @vfinale, RuntimeEpisode, Overview)
SET
Finale = NULLIF(@vfinale,'null')
;

LOAD DATA INFILE '/var/lib/mysql-files/genre.csv'
INTO TABLE GENRE
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/actor.csv'
INTO TABLE ACTOR
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/cast.csv'
INTO TABLE CAST
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/series_genre.csv'
INTO TABLE SERIES_GENRE
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;