import json
import requests
from aylienapiclient import textapi
c = textapi.Client("2362d480", "27606230dda39598ad692c0e8809285e")

related = c.Related({"phrase": "terrorism"})
relatedPhrases = []
for phrase in related['related']:
	#relatedPhrases.append(phrase['phrase'])

#for phrase in relatedPhrases:
	url="http://www.faroo.com/api?q="+phrase["phrase"]+"&start=1&length=10&l=en&src=news&f=json&key=L61Zj@aitGMws0IuAMFIyQ@nJ@A_"
	response = requests.get(url, verify=True)
	if response.status_code == 200:
		data = response.json()
		res = data["results"]
		for nw in res:
			"""extract = c.Extract({"url": nw["url"], "best_image": True})
			entities = c.Entities({"text": extract})
			for type, values in entities['entities'].items():
 				print (type,', '.join(values))"""
			summary = c.Summarize({'url': nw["url"], 'sentences_number': 5})
			articlesum = ''
			for sentence in summary['sentences']:
				articlesum+=sentence
			with open('newsData.txt', 'a') as f:
				f.write(articlesum)
			"""entities = c.Entities({"text": articlesum})
			for type, values in entities['entities'].items():
 				print (type,', '.join(values))
			print("---------------------------------------------------------------------------------------------")
	
	print("---------------------------------------------------------------------------------------------")"""
	
