# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel
import random

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

LEDdivision=(65535/LEDcount)



while True:
    reading = potentiometer.read_u16()
    LEDnumber=round(reading/LEDdivision)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    for i in range (LEDnumber):
        strand[i]=(r,g,b)
        
    for i in range(LEDnumber,LEDcount, 1):
        strand[i]=(0,0,0)
    strand.write()
    time.sleep(0.3)
        