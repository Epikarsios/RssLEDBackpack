import feedparser
import time
# Create display instance on default I2C address (0x70) and bus number.
display = AlphaNum4.AlphaNum4()

# Initialize the display. Must be called once before using the display.
display.begin()




message = 'This is an example of the 4 character alpha-numeric display. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG? the quick brown fox jumps over the lazy dog!'
pos = 0

#create feed caled Rss
Rss = feedparser.parse('http://feeds.reuters.com/Reuters/domesticNews')


#Loop to iterate through all titles in feed sleeping for 1 second between printing

for i in Rss.entries:
	print (i.title)
	time.sleep(1)
# Dashed line
	print("----------------------------------------------------------------")
    # Clear the display buffer.
    display.clear()
    # Print a 4 character string to the display buffer.
    display.print_str(i.title[pos:pos+4])
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()
    # Increment position. Wrap back to 0 when the end is reached.
    pos += 1
    if pos > len(i.title)-4:
        pos = 0
    # Delay for half a second.
    time.sleep(0.5)
