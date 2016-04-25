from aylienapiclient import textapi
c = textapi.Client("331741bd", "b5b0b3079d2220b1dfd3eeed32f8adab")

related = c.Related({"phrase": "terrorism"})
relatedPhrases = []
for phrase in related['related']:
	relatedPhrases.append(phrase['phrase'])
#print(relatedPhrases)

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = '1frw6GnZHIzkrAz6Nk8jRo2Y1'
consumer_secret = '9pkhy6Ow0m22xRMUjIjJYfd0lt4insoQTue6x3NWLqjn4rDm4B'
access_token = '4780814894-0AX6wOOG7C8FGM7FGA70tQ49rMYve73cTWUuNDc'
access_secret = 'ERUUrdWj90uOkaHgs0nsFDua5LKypfeh447YsB5cUYWOC'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweetData.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=relatedPhrases,async=True,languages=["en"])