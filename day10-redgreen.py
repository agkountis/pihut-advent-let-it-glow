# Imports
from machine import Pin
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)


# LED index list
ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    for led in ledindex:
        if led%2==0:
            strand[led]=255,0,0
        else:
            strand[led]=0,255,0
        strand.write()
    time.sleep(1)
    strand.fill((0,0,0))
    strand.write()
    time.sleep(1)
