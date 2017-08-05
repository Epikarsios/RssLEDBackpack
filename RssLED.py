import feedparser
import time
# Create display instance on default I2C address (0x70) and bus number.
from Adafruit_LED_Backpack import AlphaNum4

display = AlphaNum4.AlphaNum4()
# Initialize the display. Must be called once before using the display.
display.begin()

#create string(s) with rss address for multiple feeds 
RssAddress = "http://feeds.reuters.com/Reuters/domesticNews"

#create feed caled Rss
Rss = feedparser.parse(RssAddress)

#Loop to iterate through all titles in feed sleeping for 1 second between printing
display.clear()
display.write_display()
#Loop through each title of feed
for i in Rss.entries:
	#prints title to console
	print (i.title)
	#reset position to begining
	pos = 0
	#Change string to Uppercase for readability and add --* buffer to begining and end to distinguish titles
	CapString = "---*" +  i.title.upper() + "*---" 
       
	# Dashed line in console for aesthetics
	print("----------------------------------------------------------------")
    
#Loop for scrolling through title 	
	for x in range(0,len(CapString)-4):
    # Print a 4 character string to the display buffer.
        	display.print_str(CapString[pos:pos+4])
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
        	display.write_display()
    # Increment position. Wrap back to 0 when the end is reached.
        	pos += 1
     		if pos > len(CapString)-4:
			pos = 0
		
    # Delay for 0.15 of a second. This can be changed to speed up or slow down the scroll.
      		time.sleep(0.15)
	
# Clear out display
display.print_str("    ")
display.write_display()
