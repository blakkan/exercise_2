# exercise_2 - Storm interfaced with twitter stream

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

## Step 3:
