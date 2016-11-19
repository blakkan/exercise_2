CREATE DATABASE Tcount owner postgres;
\connect tcount
CREATE TABLE Tweetwordcount ( word VARCHAR UNIQUE primary key, count INT DEFAULT 0);
