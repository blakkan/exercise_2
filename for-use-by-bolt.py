#Sample code snippets for working with psycopg


#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

#
# upserts
#

def increment( my_word ):
    cur.execute('''UPDATE Tweetwordcount SET count=count+1 WHERE word = '{}' RETURNING count;'''.format( my_word ))
    if not cur.fetchall():   #python idiom for empty list
       cur.execute('''INSERT INTO tweetwordcount VALUES ( '{}', 1 );'''.format( my_word ))


increment('dog')
increment('dog')
increment('cat')
increment('zebra')

cur.execute("SELECT word, count from tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"


## All done
conn.close()
