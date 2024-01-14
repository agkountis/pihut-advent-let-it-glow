# Imports
import time
from machine import Pin
from neopixel import NeoPixel


# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2),1)

# Define some GRB colour variables
white = 240,140,255 #White-ish!
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238, 223, 105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215, 100, 0

colors = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

while True:
    for color in colors:
        GRBled.fill((color))
        GRBled.write()
        time.sleep(0.5)


