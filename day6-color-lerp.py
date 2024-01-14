# Imports
import time
from machine import Pin
from neopixel import NeoPixel


# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2),1)

# Define some GRB colour variables
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

colors = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

def lerp(v0, v1, t):
    return (1.0 - t) * v0 + t * v1

interval_sec = 0.001
anim_duration = 11.0
curr_time = 0.0
i0 = 0
i1 = 1
while True:
    
    time.sleep(interval_sec)
    curr_time += interval_sec
    
    i0 = int(curr_time % anim_duration)
    i1 = i0 + 1
    
    if i1 > 10:
        i1 = 0
        
    col1 = colors[i0]
    col2 = colors[i1]
    
    
    t = curr_time % 1.0
    g = int(lerp(col1[0], col2[0], t))
    r = int(lerp(col1[1], col2[1], t))
    b = int(lerp(col1[2], col2[2], t))
    
    print(g, r, b)
    
    GRBled.fill((g, r, b))
    GRBled.write()

