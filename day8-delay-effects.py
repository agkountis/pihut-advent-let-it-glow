import time
from machine import Pin
from neopixel import NeoPixel


ring = NeoPixel(Pin(2),12)

ring.fill((0,0,0))
ring.write()
time.sleep(0.5)

while True:
    for i in range(12):
        ring[i]= 0,0,10
        ring.write()
        time.sleep(0.1)
    for i in range(12):
        ring[i]= 0,0,0
        ring.write()
        time.sleep(0.1)
        