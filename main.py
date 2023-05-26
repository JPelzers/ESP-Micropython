import urequests
from machine import Pin, SoftI2C
import ssd1306
#This library is depracated, from Adafruit, it will need to be manually uploaded to the ESP (see Readme)
from time import sleep

# Set Display size (note: this is for a 128x64 OLED, should yours differ in size please change this as well as the code in where we print the text to a particular screen location 
oled_width = 128
oled_height = 64
#Create i2c object
#For this code we use the software I2C library, meaning you can use any GPIO Pin from your board
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    #API Call (Note: You need to provide your own API Key and the Station ID of your preferred station, you may request this and see a list of station IDs at: https://www.transitchicago.com/developers/ttdocs/
    response = urequests.get('https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={PUT_YOUR_API_KEY_HERE}&mapid={PUT_YOUR_STATION_ID_HERE}&outputType=JSON')
    #turn response into JSON object
    parsed = response.json()
    #Determine the number of trains for which there is information available
    lastTrain = (len(parsed["ctatt"]['eta']))
    #For each available train, write the destiniation location and arrival time
    for i in range (lastTrain):
        #Clear the OLED
        oled.fill(0)
        #Parse JSON for the arrival times for each train
        txt = parsed["ctatt"]['eta'][i]['arrT']
        #split the date from the arrival time
        txt = txt.split("T")
        #Get the station name
        station = (parsed["ctatt"]['eta'][i]['staNm'])
        #Get the station color
        LineColor = (parsed["ctatt"]['eta'][i]['rt'])
        StationLineColor = station + " " + LineColor
        #Print all of the above to the screen atthe specified location
        text = (parsed["ctatt"]['eta'][i]['destNm'] + ":")
        oled.text(StationLineColor, 0, 0)
        oled.text(text, 0 , 25)
        oled.text(txt[1], 25, 50)
        oled.show()
        sleep(3)
        #This loops through all of the available times and starts over

