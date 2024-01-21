import time
from machine import Pin
from neopixel import NeoPixel


ring = NeoPixel(Pin(2),12)

ring.fill((0,0,0))
ring.write()
time.sleep(0.5)


while True:
    for i in range(12):
        ring[i]= 5,0,5
        ring.write()
        time.sleep(0.1)
        ring.fill((0,0,0))
        ring.write()
    for i in reversed (range(12)):
        ring[i]= 5,0,5
        ring.write()
        time.sleep(0.1)
        ring.fill((0,0,0))
        ring.write()