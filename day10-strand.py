# Imports
from machine import Pin
from neopixel import NeoPixel
import time

# Define the strand pin number (2) and number of LEDs (15)
strand = NeoPixel(Pin(2), 15)

# Fill with red for 10 seconds
strand.fill((50,0,0))
strand.write()
time.sleep(5)

# Turn off
strand.fill((0,0,0))
strand.write()
