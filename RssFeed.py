import feedparser
import time

#create feed caled Rss
Rss = feedparser.parse('http://feeds.reuters.com/Reuters/domesticNews')

# Prints News + Logo

print ("Here Comes The News ")
print ("  *  ")
time.sleep(.2)
print (" * * ")
time.sleep(.2)
print ("*   *")
time.sleep(.2)
print (" * * ")
time.sleep(.2)
print ("  * ")
print ("**************************************************************")
#Loop to iterate through all titles in feed sleeping for 1 second between printing

for i in Rss.entries:
	print (i.title)
	time.sleep(1)
# Dashed line
	print("-----------------------------------------------------------------")


