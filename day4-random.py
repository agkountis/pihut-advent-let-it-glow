from machine import Pin
import time
import random


segments = [
    Pin(13, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(9, Pin.OUT),
]

while True:
    
    r = random.randint(0,4) # set r to a random number between 0 and 4
    
    segments[r].value(1) # light the segment from the list with the index of r
    
    time.sleep(0.1)
    
    segments[r].value(0) # Turn off the same LED
