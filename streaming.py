from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pdb
# from ast import literal_eval
import json
import time
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, count, l1, n):
        self.count=count
        self.l1=l1
        self.n=n
        self.oldtime=time.time()

    def on_data(self, tweet):
        tweet=json.loads(tweet)
        # pdb.set_trace()
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
        self.l1.append(l2)
        self.count=self.count+1
        print(time.time()-self.oldtime)
        if self.count==self.n or time.time()-self.oldtime>120:
            return False
        # i=i+1
        # print(data)
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            return False

# if __name__ == '__main__':
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)

#     stream = Stream(auth, l)
# stream.filter(track=['modi'])

def twit(keyword,n):
    l1=[]
    l = StdOutListener(0,l1,n)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=keyword)
    return l.l1