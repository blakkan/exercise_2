from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2



class WordCounter(Bolt):

    #helper subroutine
    def increase_a_word_count( self, my_word, how_much_to_increase = 1 ):
        my_word_cleaned = my_word.replace("'", "''")
        self.cur.execute('''UPDATE "Tweetwordcount" SET count=count+%s WHERE word = '%s' RETURNING count;''' % (how_much_to_increase, my_word_cleaned) )
        if not self.cur.fetchall():   #python idiom for empty list
           self.cur.execute('''INSERT INTO "Tweetwordcount" VALUES ( '%s', %s );''' % (my_word_cleaned, how_much_to_increase) )
        self.conn.commit() #This might be expensive in the long run.


    def initialize(self, conf, ctx):
        self.counts = Counter()

        #added connect to the database and establish a locla cursor.
        try:
          self.conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
        except:
          self.log("Could not connect to the database.  I blame society.")
          exit()
        self.cur = self.conn.cursor()


    def process(self, tup):
        word = tup.values[0]

        self.increase_a_word_count(word)

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.


        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
