#! /usr/bin/python
#
# top10.py
#
#   Simple script to produce a .csv file of the top 20 words in the database, along with
# their counts.   They are given in descending order of count.
#
#   This is used to produce the bar chart of counts.
#
#   Output ist to stdout, so pipe it to where you want it...
#

import psycopg2

#
# For this exercise, we use fixed names of databases, users, and tables.
#
try:
  conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
except:
  print "Could not connect to the database.  I blame society."
  exit()

cur = conn.cursor()

#
# Get the records and construct a csv output
#


cur.execute('''SELECT word, count FROM "Tweetwordcount" ORDER BY count DESC LIMIT 20;''')

records = cur.fetchall()

print "Word,Count"
for rec in records:
   print '''"%s",%d''' % (rec[0], rec[1])  #remake it as a tuple, not a list

