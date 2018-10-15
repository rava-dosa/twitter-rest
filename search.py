from TwitterSearch import *
import time

def twit(keyword,n):
	l1=[]
	try:
		# pdb.set_trace()
		tso = TwitterSearchOrder() # create a TwitterSearchOrder object
		tso.set_keywords(keyword) # let's define all words we would like to have a look for
		# tso.set_language('en') # we want to see German tweets only
		tso.set_include_entities(True) # and don't give us all those entity information

		# it's about time to create a TwitterSearch object with our secret tokens
		ts = TwitterSearch(
			consumer_key = '',
			consumer_secret = '',
			access_token = '',
			access_token_secret = ''
		 )

		 # this is where the fun actually starts :)
		i=0
		for tweet in ts.search_tweets_iterable(tso):
			if(i==n):
				break
			# print(tweet)
			# print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
			id1=tweet["id"]
			text=tweet['text'].replace('\n','')
			text=text.replace('@','')
			text=text.replace("'","")
			# text=text.strip(";")
			username=tweet['user']['screen_name']
			name=tweet['user']['name']
			followers_count=tweet['user']['followers_count']
			# followers_count=tweet['user']['followers_count']
			favourites_count=tweet['user']['favourites_count']
			retweet_count=tweet['retweet_count']
			favorite_count=tweet['favorite_count']
			language=tweet['lang']
			# datetime=tweet['created_at']
			datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
			l2=[id1,text,username,name,followers_count,favourites_count,language,datetime,retweet_count,favorite_count]
			# print(l2)
			l1.append(l2)
			i=i+1


	except TwitterSearchException as e: # take care of all those ugly errors if there are some
		print(e)
	# print (l1)
	return l1