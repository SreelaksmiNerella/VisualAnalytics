
from aylienapiclient import textapi
c = textapi.Client("2362d480", "27606230dda39598ad692c0e8809285e")

with open('newsDataGname.txt') as f:
	lines = f.read().splitlines()
entities = c.Entities({"text": lines})
for type, values in entities['entities'].items():
	print (type,', '.join(values))
