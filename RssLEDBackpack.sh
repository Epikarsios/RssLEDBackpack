#! /bin/bash

# 
# RssLEDBackpack
# ========
# A RssLED installer for raspberry pi users.
# 
# https://github.com/Epikarsios/RssLEDBackpack
# 
# All code is copyright (c) Epikarsios 2017
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
# 
# 


echo "Updating all existing packages..."
sudo apt-get -y update
echo "..........................................."
echo "Installing Python Libraries"
sudo apt-get install -y build-essential python-dev python-smbus python-pip  python-imaging git
echo "Installing Adafruit LEDBackpack Libraries"
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
echo  "Running Adafruit Install \n"
sudo python setup.py install 
echo "Getting Feedparser "
sudo pip install feedparser
cd ..
rm -r Adafruit_Python_LED_Backpack

echo "Done! Run the Rss with python RssLED.py "
echo "Default Rss Feed is Reuters US Domestic News"
echo "sudo nano RssLED.py to edit which feed"
exit 0
