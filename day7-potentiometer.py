# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

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

reading = 0

while True: # Loop forever
    reading = potentiometer.read_u16()
    time.sleep(0.1)
    if reading<=20000:
        GRBled1.fill((red))
        GRBled1.write()
    elif 20000<reading<40000:
        GRBled1.fill((orange))
        GRBled1.write()
    elif reading>=40000:
        GRBled1.fill((green))
        GRBled1.write()
    if reading<=10000:
        GRBled2.fill((blue))
        GRBled2.write()
    elif 10000<reading<30000:
        GRBled2.fill((white))
        GRBled2.write()
    elif reading>=30000:
        GRBled2.fill((bogey))
        GRBled2.write()