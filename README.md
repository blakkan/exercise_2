# exercise_2 - Storm interfaced with twitter stream

# This is not the Readme.txt file; see that file for full details.
# This file is just for convenient reference on github 

## Step 1: Environment and tool setup

The big Problem here was that the lab directions indicated we should name the Streamparse project
EX2TweetwordCount.  The finding was that you cannot have a digit in this project name.  Workaround
is to call it EXtwotweetwordcount (i.e., spell out "two" instead of "2" in the project name).

Twitter setup was relatively uneventfull; did need to add phone number (It's not optional if you
want to register an application... Optional if you only want a twitter account)

## Step 2: Tweepy Install/Twitter application setup.

Note this is a bit of a misnomer; we're not actually writing an applciation that runs on Twitter.
We're registering with twitter and obtaining access keys with which our (Amazon EC2-hosted) storm
application will be able to receceived a stream of tweets.

Test run a provided application which pulls over one minute of tweets (silently, you need to be
patient for one minute...).  Running at 8:38am on November 19, 2016,
the test application gave 3148 tweets.

Also test run the application on EC2.   (Initially, try a very simplifed version which does not
employ any parallelism in storm; will add that later.  Also adding logging helps to see that it's
working)  Just go into the directory (EXtwotweetwordcount)
and execute "sparse run."  There are lots of words, plus "Empty queue exceptions" shown.
A few points in the data- there isn't uniform casing of the words.  There are also some non-word
patterns making it through the filter (this could be cleaned up later).

## Step 3:  Application deployment and running

To initialize, run the script 

Application downcases everything, does a modest trimming out of obvious non-words (but twitter users
are pretty clever in creating interresting things to parse out.  I chose to leave them for now).

We do permit the apostrphe (single quote) to appear in words.   This has implications in later analysis, since
SQL commands will need those doubled in order to escape them.

To run the application, cd into EXtwotweetwordcount, then sparse run.

## Step 4: Results presentation

The results are left in the database (username=postgres, database=Tcount, table=Tweetwordcount).
cd back up to the main project directory and run 

finalresults.py (With or without a single wordcommand line argument.  Remember to double quote any word containing an apostrophe)  

Also run histogram.py (With two integer aguments.)  

Plot.png is also included.   The assignment didn't indicate this needed to be auto-generated, so I chose to 
generate it outside the EC2 instance, using R running on my local development machine.  (Note
that I mount the instance file system on my development machine).  To produce the plot, I ran
my own script top20tocsv.py to produce a csv file, then directed the csv file into R running the makeplot.r
script.  (The plot is in the minimalist "Tufte" style taught in W203.)  Note that this always writes its output
to Plot.png.

python top20tocsv.py > words.csv  #on the instance
r makeplot.r < words.csv          #I run this on my local machine

