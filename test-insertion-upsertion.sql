INSERT INTO Tweetwordcount VALUES ( 'dog', 1 );
INSERT INTO Tweetwordcount VALUES ( 'cat', 1 );
SELECT * FROM Tweetwordcount;

-- upserts

-- if this returns one row (with the count), then we're good.  Otherwise need to create
UPDATE Tweetwordcount SET count=count+1 WHERE word = 'dog' RETURNING count;

UPDATE Tweetwordcount SET count=count+1 WHERE word = 'zebra' RETURNING count;





SELECT * FROM Tweetwordcount;
