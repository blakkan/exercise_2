### exercise_2 - Storm interfaced with twitter stream

# Step 1: Environment and tool setup

The bit pbolem here was that the lab directions indicated we should name the Streamparse project
EX2TweetwordCount.  The finding was that you cannot have a digit in this project name.  Workaround
is to call it EXtwotweetwordcount (i.e., spell out "two" instead of "2" in the project name).

# Step 2: Tweepy Install/Twitter application setup.

Note this is a bit of a misnomer; we're not actually writing an applciation that runs on Twitter.
We're registering with twitter and obtaining access keys with which our (Amazon EC2-hosted) storm
application will be able to receceived a stream of tweets.

Also test run the application on EC2.   (Initially, try a very simplifed version which does not
  employ any parallelism in storm; will add that later.)

# Step 3:
