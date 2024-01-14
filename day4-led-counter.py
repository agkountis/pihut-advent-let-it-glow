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

# Set up our button name and GPIO pin number
# Set the pin as an input and use a pull down
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

count = -1

for seg in segments:
    seg.value(0)

while True:
    
    time.sleep(0.01) # Short delay to avoid the program running too fast
    
    if redButton.value() == 1: # If red button pressed
        
        if count == 4: # If the count is already 4
            pass # Do nothing
            
        else:
            count = count + 1 # Add 1 to our counter
            segments[count].value(1) # Light the LED index for the count
            time.sleep(0.2)
            
    if greenButton.value() == 1: # If green button pressed
        
        if count == -1: # If count is already -1
            pass # Do nothing
            
        else:   
            segments[count].value(0) # Turn off the LED index for the count
            time.sleep(0.2)
            count = count -1 # Remove 1 from our counter
    