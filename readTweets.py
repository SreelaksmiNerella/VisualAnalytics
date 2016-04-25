import json
from aylienapiclient import textapi

client = textapi.Client("2362d480", "27606230dda39598ad692c0e8809285e")

tweets_data_path = 'tweetData.json'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

tweetsText = list(map(lambda tweet: tweet['text'], tweets_data))
for twt in tweetsText:
	with open('tweetText.txt', 'a') as f:
		#print(twt+"\n")
		f.write(twt+"\n")
"""print(len(tweetsText))

for text in tweetsText:
	entities = client.Entities({"text": text})
	for type, values in entities['entities'].items():
  		print(type,', '.join(values))
	print("---------------------------------------------------------------------------------------------")
"""