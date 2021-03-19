# Finding topics of interest by using the filtering capablities it offers.
import twitter
import json
import sys
import csv

csvfile = open('IPL.csv','a')
csvwriter = csv.writer(csvfile)
 
# == OAuth Authentication ==
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "Keys and tokens")
 # PUT YOUR KEYS AND SECRETS IN HERE, IT WONT WORK WITHOUT YOUR KEYS FROM TWITTER !!!!!
consumer_key="8qHBAaHqXmZxSWf4xT1iUZpY1"
consumer_secret="kQOVSvIlYl4A2IbypZpFOopIyafURdBg5PDYO3A0HHguYD6hlJ"
 
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1163418747501043712-WobA4YkAzXVcKfRc6h6QQ0ONKsWH5U"
access_token_secret="2eks7joqEAvKlTVuKd3CIwQhkultJaGaQEeTK0w2wDtut"
 
auth = twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)
# Query terms
q = '#Lampard' # Comma-separated list of terms, start with something busy to test your script, then once you know its working put your hashtags in, max 400 tags
print('Filtering the public timeline for track=',q)
# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
# See 
stream = twitter_stream.statuses.filter(track=q)
# For illustrative purposes, when all else fails, search for a relevant topic such as Madonna
# and something is sure to turn up (at least, on Twitter)
# note that stream is a special never ending list so this loops non stop
# to stop it type CMD-C at the terminal where its running
for tweet in stream:
	# what is this thing called a tweet?
	# its a structured object in JSON format. We can treat this as a python dictionary - http://learnpythonthehardway.org/book/ex39.html
	# sometimes it helps to dump an entire tweet using the line below so you can see the names of the fields
	# print json.dumps(tweet, indent=1')
	print(tweet['text'])
	
	csvwriter.writerow([tweet['text'].encode('utf-8'),tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']])
	
	


