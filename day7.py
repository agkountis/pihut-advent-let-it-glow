# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the RGB LEDs
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)


GRBled1.fill((0,0,0)) # All zero = no light!
GRBled1.write()
GRBled2.fill((0,0,0)) # All zero = no light!
GRBled2.write()