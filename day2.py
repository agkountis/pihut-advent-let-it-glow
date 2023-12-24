# Imports
from machine import Pin
import time

# Pin setup
red = Pin(14, Pin.OUT) # Set GPIO as an output

for i in range(10): # Loop 10 times
    red.value(1) # LED on
    time.sleep(0.5) # Wait half a second.
    
    red.value(0) # LED off
    time.sleep(0.5)	# Wait half a second.
    
    print("Flash!")

print("Program finished")
