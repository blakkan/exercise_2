#Sample code snippets for working with psycopg


#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2

try:
  conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
except:
  print "Could not connect to the database.  I blame society."
  exit()

cur = conn.cursor()

#
# upserts
#

def increase_a_word_count( cursor, my_word, how_much_to_increase = 1 ):
    cur.execute('''UPDATE "Tweetwordcount" SET count=count+%s WHERE word = '%s' RETURNING count;''' % (how_much_to_increase, my_word) )
    if not cur.fetchall():   #python idiom for empty list
       cur.execute('''INSERT INTO "Tweetwordcount" VALUES ( '%s', %s );''' % (my_word, how_much_to_increase) )
    cursor.connection.commit() #This might be expensive in the long run.


increase_a_word_count(cur, 'dog')
increase_a_word_count(cur, 'dog', 2)
increase_a_word_count(cur, 'cat', 5)
increase_a_word_count(cur, 'zebra')

cur.execute('''SELECT word, count from "Tweetwordcount"''')
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"


## All done
conn.close()
