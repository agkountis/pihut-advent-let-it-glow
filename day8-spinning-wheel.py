import time
from machine import Pin
from neopixel import NeoPixel
import random

ring = NeoPixel(Pin(2),12)

ring.fill((0,0,0))
ring.write()
time.sleep(0.5)

while True:
    r = random.randint(0,100)
    g = random.randint(0,100)
    b = random.randint(0,100)
    for i in range(12):
        ring[i]= (r,g,b)
        ring.write()
        time.sleep(0.1)