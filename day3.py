# Imports
from machine import Pin
import time

# onboardLED = Pin(25, Pin.OUT)
redLED = Pin(14, Pin.OUT)

# Set up our button name and GPIO pin number
# Set the pin as an input and use a pull down
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

HIGH = 1

count = 0
while True:
    time.sleep(0.2) # Short delay to avoid multiple inputs from a single press
    redLED.value(0) # LED off until button press
    
    if redButton.value() == HIGH:
        count -= 1
        redLED.value(1) # LED on
        print(count)
    
    if greenButton.value() == HIGH:
        count += 1
        redLED.value(1) # LED on
        print(count)
