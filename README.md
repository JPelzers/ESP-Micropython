# ESP32-Micropython_ChicagoCTA_NextStop

This is code to run a neat program on an ESP-32 microcontroller that displays the arrival times of the next tracked trains at any of the Chicago CTA Train stations.

Requirements:
- A computer with a text editor and the ability to upload via USB serial to an ESP-32
- An ESP32 Chip with the micropython firmware: https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro
- An OLED Display, for this project I use one that is 128x64 monocolor but as long as it is supported by the Adafruit SSD1306 library you are fine with some minor code modifications (mentioned in the code comments)
- The wires and/or breadboard to connect the four necessary wires from the ESP-32 to the OLED screen
- An API key from the CTA and a Station ID for the station you would like to see the times for from: 
https://www.transitchicago.com/developers/ttdocs/ (you will need to request an API key but the requests is granted immediately)

Directions:

1. Follow the instructions from the https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro guide and get a REPL on your ESP-32

2. Connect your OLED to your board, we are using the Software I2C library, so you can choose any ports for the SDA/SCL, but for my code I use the folling pinout:
- ESP 32 3.3v to OLED VCC
- ESP Ground to OLED GND
- ESP D21 to OLED SDA
- ESP D22 to OLED SCL

3. Download the files from this project (boot.py, main.py, ssd1306.py)

4. Once you have access to the REPL, follow the following instructions to get a WebREPL: https://www.techcoil.com/blog/how-to-setup-micropython-webrepl-on-your-esp32-development-board/ 

  **Note:** The port they use in the above example is different from what yours will likely be, mine in Linux is "/dev/ttyUSB0", in addition you may need to install rshell/nano

  **Another Note**: The "boot.py" in this project folder is the same code as the code in the above tutorial, you just need to change the SSID and the Password to your own network's

5. Modify boot.py with your SSID and Password

6. Modify main.py with your API Key and the station number of your desired station (make sure there are no {} in the code)

7. Upload boot.py, main.py, and ssd1306.py

8. Get to your train on time!
