import sys
import re
import psycopg2


# Do some very simple command-line argument validation
print sys.argv

if len(sys.argv) == 3: #space separated
    low_number = int(sys.argv[1])
    high_number = int(sys.argv[2])
else:
    print "Usage: %s [number number]"
    exit()

if ( low_number > high_number ):
    print "First number cannot exceed second number"
    exit()

# Do just a little more, just to prevent somebody from easily doing any sql injection...
##  There are better ways to do this (and that pesky single quote is currently permitted here)
new_word = re.sub(r'[\;\"\,\)\(]', '', the_word)

if the_word != new_word:
    print "I won't let you try that word.  I would be willing to let you try %s" % new_word
    exit()

try:
  conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
except:
  print "Could not connect to the database.  I blame society."

cur = conn.cursor()

#could use "like" instead of = here, if we wanted to permit sql regex matching...
sql_command = '''SELECT word, count FROM "Tweetwordcount" WHERE word = '%s'; ''' % new_word

cur.execute(sql_command)
records = cur.fetchall()
print '''Total number of occurences of "%s": %d''' % ( new_word, len(records) )
