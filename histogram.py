#! /usr/bin/python
#
# histogram.py
#
#   Given two integers (from the command line), retuans all the words for which have 
# occurance counts between the two integers (inclusive)
#

import sys
import re
import psycopg2


# Do some very simple command-line argument validation; we need to get two integers

if len(sys.argv) == 3: #space separated
    low_number_string = sys.argv[1].replace(",", "")
    high_number_string = sys.argv[2]
elif len(sys.argv) == 2:
    low_number_string, high_number_string = sys.argv[1].rsplit(",", 2)
else:
    print "Usage: %s [number number] or [number,number]"
    exit()

low_number = low_number_string.strip()
high_number = high_number_string.strip()

if (not low_number.isdigit()) or (not high_number.isdigit()):
    print "Arguments must be numeric"
    exit()


if ( int(low_number) > int(high_number) ):
    print "First number cannot exceed second number"
    exit()

#
# Connect to the database or die in the attempt.
#

try:
  conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
except:
  print "Could not connect to the database.  I blame society."

cur = conn.cursor()

#could use "like" instead of = here, if we wanted to permit sql regex matching... but that's beyond what we need.
sql_command = '''SELECT word, count FROM "Tweetwordcount" WHERE count >= %s AND count <= %s ORDER BY count DESC, word ASC''' % (low_number, high_number)

cur.execute(sql_command)
records = cur.fetchall()
for line in records:
    print "%20s: %d" % (line[0], line[1])   #turn the list of two items back into a tuple, for strict conformance
