from machine import Pin
import time


segments = [
    Pin(13, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(9, Pin.OUT),
]

redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

HIGH = 1
LOW = 0
index = 0
inc = 1

currentSegment = segments[0]
prevSegment = segments[0]
while True:
    if greenButton.value() == HIGH:
        time.sleep(0.2)
        for seg in segments:
            seg.value(LOW)
    
    time.sleep(0.08)
       
    currentSegment = segments[index]
    currentSegment.value(HIGH)
    print("current", index)
    
    prevIndex = index - inc
    print("prev", prevIndex)
    if prevIndex >= 0:
        segments[prevIndex].value(LOW)
    
    if index == 4:
        inc = -1
    
    if index == 0:
        inc = 1
       
    print("---")
        
    index += inc
        
    
