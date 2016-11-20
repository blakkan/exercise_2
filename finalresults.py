#
# finalresults.py
#
#   Extracts the word counts from the table in the database.
# For purposes of this exercise, the user information, database, and table are all 
# fixed and hard coded
#
#

import sys
import re
import psycopg2


# Do some very simple command-line argument validation
if len(sys.argv) > 2:
    print "You must call this program with either a single argument or none (for all words)"
    exit()

# If we're given an argument, check it a little more
if len(sys.argv) == 2:
  the_word = sys.argv[1]

  # Do just a little more validation, just to prevent somebody from easily doing any sql injection...
  ##  There are better ways to do this (and that pesky single quote is currently permitted here)
  new_word = re.sub(r'[\;\"\,\)\(]', '', the_word)

  if the_word != new_word:
    print "I won't let you try that word.  I would be willing to let you try %s" % new_word
    exit()

#
# Open the database
#

try:
  conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
except:
  print "Could not connect to the database.  I blame society."

cur = conn.cursor()

# We Could use "like" instead of = here, if we wanted to permit sql regex matching... But probably faster
# to just make this decision about what SQL command to send once.
# The "replace" is here to double any single-quotes to escape them in the SQL command.  This is because
# we consider words like "won't" to be legitimate.

if len(sys.argv) == 2:
  sql_command = '''SELECT word, count FROM "Tweetwordcount" WHERE word = '%s';''' % new_word.replace("'", "''")
else:
  sql_command = '''SELECT word, count FROM "Tweetwordcount" ORDER BY word ASC;'''

# Send the command and get the results

cur.execute(sql_command)
records = cur.fetchall()

# The presentation of results differs between the "argument" version and the "non-argument" version
if len(sys.argv) == 2: #argument version

  if len(records) == 0:
    the_count = 0
  else:
    the_count = records[0][1]
  print '''Total number of occurences of "%s": %d''' % ( new_word, the_count )

else:

  for line in records:
    print "%20s: %d" % (line[0], line[1])   #turn the list of two items back into a tuple, for strict conformance
