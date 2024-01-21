# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel
import random


potentiometer = ADC(Pin(28))

GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

flash = 0
reading = 0

while True:
    reading = potentiometer.read_u16()
    flash = reading/65535
    # Generate random GRB values
    g = random.randint(0,255)
    r = random.randint(0,255)
    b = random.randint(0,255)
    GRBled1.fill((g,r,b))
    GRBled1.write()
    time.sleep(flash)