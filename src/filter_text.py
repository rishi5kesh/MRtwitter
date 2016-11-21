import json
import codecs

# open the downloaded tweet file
with open('cars.json', 'r') as f:
	

# open a file for writing output
   fo = codecs.open("filtertext.txt", encoding='utf-8', mode='w+')
    
#iterate through the tweet file to extract only text values from the json and write to the result file
   for line in f:
   		tweet = json.loads(line)	
   		
   		if tweet.get("text", '') == '':
   			continue
   		tweet["text"] = tweet["text"].replace('\n', '')
   		x = tweet["text"]
   		fo.write(x)

   		fo.write("\n")

fo.close()
   	
