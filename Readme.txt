To run the application:

Step 0:

This assumes they python psycopg2 module has already been installed with pip.
The authorization keys for twitter are already established, and saved in the
appropriate file in the project, so nothing need be set up with respect to 
twitter.  If you don't have it, do this:

$pip install psycopg2


Step 1:

From the project's main directory, setup the database (and table) with this command.
(Note the use of double quotes in the script to maintain the cases of the database
and the table).  This command will remove any existing database before re-creating
it, so only run it if you no longer need (or have otherwise kept) your own data.

$python create-database.sh



Step 2:

Enter the streamparse project directory with this command:

$cd EXtwotweetwordcount




Step 3:

Start the streamparse application with the following command.  Note that the 
streamparse application will run until halted with a "control-c."  I typically let
it run for about 5 minutes.  My design does not (by design) include a fixed timer.
So control-c to stop it (or send a kill signal) when you have enough data.
I use the topp20tocsv.py script running in a separate ssh session to
 monitor it as it runs, and use that to decide when I have sufficient data.

$sparse run



Step 4:

At this point, the Table "Tweetwordcount" in Database "Tcount" (owned by postgres)
has been created.  By design, all letters have been lowercased, and many (but not all)
special words have been filtered out (i.e. "RT for ReTweet is removed before downcasing).

While still in the streamparse project dirctory, run these commands: (adjusting the
word to be searched for, and the histogram counts based on preference).

$python ../finalresults.py the
$python ../histogram.py 500,99999



Optional Step 5:

The exact method of creating the Plot.png file is not specified in the exercise.  I
use a script (which can be run as follows) to generate the counts of the top-20
occuring words in csv format.  (I later use this in an offline process to create the plot
using R).

$python ../top20tocsv.py


Final comments and observations:

A) Projects can't, apparently, have a digit in their name.   Thus instead of 
EX2tweetwordcount I used EXtwotweetwordcount.   It seems an unusual and arbitrary restriction.

B) In postgres, it is necessary to use double quotes around database names and table names
in SQL statments in order to preserve the case of letters (otherwise, they all get downcased)

C) The assignment didn't explicitly say to do it, but I down-cased all words, so (for example)
"I" and "i" (both commonly seen) would map to "i".

D) I decided to keep the apostrophe as part of words, so that needs to be accomodated in SQL
statements (I used routines to escape them by doubling them).

E) Tweets with words containing backslashes are a bad thing.   I cleaned the data by fairly
crudely squeezing them out with code like this:

aword = word.strip("\"?><,'.:;)").replace("\\", "").lower()

in the parser.  For a real production system, even more care would have to be taken.   Given
the huge number of tweets, there is certain to be intentional or unintentionsl "SQL injection"
with escape characters in messages.

F) The config file has the number of parallel spouts and bolts indicated in the figure, but
admittedly does not use stream id's and/or directed streams to exactly match the streams in
the figure.

G) We have a rather old version of postgres in our class AMIs (8.4).  It doesn't support the
"Upsert" (i.e. update or insert) operation supported in the 9-series.  I added a function providing
this capability to the count bolt.

H) I do most of my development for the class (from about the 6th week) by mounting the EC2
file system on my local ubuntu machine, then using gedit (and atom) editors running on ubuntu.
(all the actual execution takes place on the EC2 centos instance, of course).  Experience is
that it works reasonably well, but the atom editor sometimes crashes becuse of the slow speed
of the ssh file system.  gedit is quite reliable.   In one of my screenshots I show both of
my screens, with windows/gitbash/ssh running my commands on the left, and ubuntu running on 
the right.   I also used R (which I already had on Ubuntu) to generate the bar graph, as the
assignment didn't require it be done on the instance.
