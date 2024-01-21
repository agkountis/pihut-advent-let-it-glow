import time
from machine import Pin
from neopixel import NeoPixel


ring = NeoPixel(Pin(2),12)

ring.fill((0,0,0))
ring.write()
time.sleep(0.5)

white = 240,140,255 #White-ish!
green = 0,255,0
red = 255,0,0
blue = 0,0,255

while True:
    ring[0] = white
    ring[1] = green
    ring[2] = red
    ring[3] = blue
    ring[4] = white
    ring[5] = green
    ring[6] = red
    ring[7] = blue
    ring[8] = white
    ring[9] = green
    ring[10] = red
    ring[11] = blue
    ring.write()
    time.sleep(0.5)
    ring.fill((0,0,0))
    ring.write()
    time.sleep(0.5)
    
