from machine import Pin
import time


segments = [
    Pin(13, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(9, Pin.OUT),
]

while True:

    # For loop to turn each LED on then off in order of the list
    for led in segments:
        
        led.value(1)
        time.sleep(0.08)
        led.value(0)
        
    # For loop in reverse, running backwards through the list
    for led in reversed (segments):
        
        led.value(1)
        time.sleep(0.08)
        led.value(0)