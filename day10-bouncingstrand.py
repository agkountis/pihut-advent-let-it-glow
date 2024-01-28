import time
from machine import Pin
from neopixel import NeoPixel

ledcount=15
GPIOnumber=2
mycolour= 255,0,0

strand = NeoPixel(Pin(GPIOnumber),ledcount)

strand.fill((0,0,0))
strand.write()
time.sleep(0.5)


while True:
    for i in range(ledcount):
        strand[i]= mycolour
        strand.write()
        time.sleep(0.1)
        strand.fill((0,0,0))
        strand.write()
    for i in reversed (range(ledcount)):
        strand[i]= mycolour
        strand.write()
        time.sleep(0.1)
        strand.fill((0,0,0))
        strand.write()