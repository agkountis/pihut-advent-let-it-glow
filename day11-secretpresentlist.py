from machine import Pin
import time

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

blockLED = Pin(6, Pin.OUT)

state = 0

passcode=[2,3,4,1]
entrycode=[]

def appending(key):
    global state
    print("*", end="")
    entrycode.append(key)
    state=1

while len(entrycode)<4:
    if state==0:
        if key1.value() == 1:
            appending(1)
        elif key2.value() == 1:
            appending(2)
        elif key3.value() == 1:
            appending(3)
        elif key4.value() == 1:
            appending(4)
    elif state == 1 and key1.value() == key2.value() == key3.value() == key4.value() == 0:
        state=0
    time.sleep(0.1)

if entrycode[0]== passcode[0]and entrycode[1]==passcode[1] and entrycode[2]==passcode[2] and entrycode[3]==passcode[3]:
    print("Secrect list")
    print("\nBarbie doll")
    print("toy truck")
    print("PS5")
    blockLED.value(1)
    time.sleep(2)
    blockLED.value(0)
else:
    print("wrong code!!")
