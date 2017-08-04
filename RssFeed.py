import feedparser
import time

#create feed caled Rss
Rss = feedparser.parse('http://feeds.reuters.com/Reuters/domesticNews')

#Loop to iterate through all titles in feed sleeping for 1 second between printing

for i in Rss.entries:
	print (i.title)
	time.sleep(1)
# Dashed line
	print("-----------------------------------------------------------------")


