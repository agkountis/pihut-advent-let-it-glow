from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from neopixel import NeoPixel
import time
import random

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

# Define LCD I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

strand.fill((0,0,0))
strand.write()
time.sleep(1)

def scrolltext(text):
    text=text+(16*" ")
    while True:
        lcd.move_to(0,0)
        lcd.putstr(text[:16])
        time.sleep(0.5)
        text=text[1:]+text[0]
        print(text)
        colorchange()

def colorchange():
    lcd.clear()
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    strand.fill((r,g,b))
    strand.write()
    time.sleep(0.5)

scrolltext("Jingle bells, jingle bells, jingle all the way!!")
    