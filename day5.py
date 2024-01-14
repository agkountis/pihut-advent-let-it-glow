# Imports
from machine import Pin
import time


switches = [
    Pin(6, Pin.IN, Pin.PULL_DOWN),
    Pin(5, Pin.IN, Pin.PULL_DOWN),
    Pin(4, Pin.IN, Pin.PULL_DOWN),
    Pin(3, Pin.IN, Pin.PULL_DOWN),
    Pin(2, Pin.IN, Pin.PULL_DOWN),
]

segments = [
    Pin(13, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(9, Pin.OUT),
]

dictionary = {
    switches[0]:segments[0],
    switches[1]:segments[1],
    switches[2]:segments[2],
    switches[3]:segments[3],
    switches[4]:segments[4]
}

    
while True:
    for switch in dictionary:
        segment = dictionary[switch]
        segment.value(switch.value())
        
    time.sleep(0.5)
            

