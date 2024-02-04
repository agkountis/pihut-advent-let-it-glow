from machine import Pin
from neopixel import NeoPixel
import time

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs
strand = NeoPixel(Pin(GPIOnumber), LEDcount)


strand.fill((0,0,0))
strand.write()

def strandfunction(colour1, colour2, colour3):
    strand.fill((colour1,colour2,colour3))

while True:
    
    if key1.value() == 1:
        strandfunction(255,255,255)

    if key2.value() == 1:
        strandfunction(0,0,255)
        
    if key3.value() == 1:
        strandfunction(0,255,0)
    
    if key4.value() == 1:
        strandfunction(255,0,0)
    strand.write()
    time.sleep(0.3)