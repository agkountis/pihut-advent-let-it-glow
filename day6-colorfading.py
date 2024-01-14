# Imports
import time
from machine import Pin
from neopixel import NeoPixel


# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2),1)


while True:
    for i in range(255):
        GRBled.fill((0, 0, i))
        GRBled.write()
        time.sleep(0.005)
        
    for i in reversed(range(255)):
        GRBled.fill((0, 0, i))
        GRBled.write()
        time.sleep(0.005)
        

