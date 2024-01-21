# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

GRBled1.fill((0,0,0))
GRBled1.write()
reading = 0
converted = 0

while True:
    reading = potentiometer.read_u16()
    converted = round(reading * (255/65535))
    GRBled1.fill((0,0,converted))
    GRBled1.write ()
    time.sleep(0.1)
    
    