from machine import Pin, I2C
import time
from neopixel import NeoPixel
from dgt20 import DHT20

# Set up I2C pins
i2c1_sda = Pin(14)
i2c1_scl = Pin(15)

# Set up I2C
i2c1 = I2C(1, sda=i2c1_sda, scl=i2c1_scl)

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)


ring = NeoPixel(Pin(2),12)

LEDdict={
    18:0,
    19:1,
    20:2,
    21:3,
    22:4,
    23:5,
    24:6,
    25:7,
    26:8,
    27:9,
    28:10,
    29:11 }

while True:
    temperature=round(dht20.measurements['t'])
    if temperature not in LEDdict:
        pass
        print("Out of temperature range")
    else:    
        LEDindex=(LEDdict[temperature])
        ring[LEDindex]= (10,0,0)
        ring.write()
        print(f"Temperature: {temperature}from machine import Pin, I2C
import time
from neopixel import NeoPixel
from dgt20 import DHT20

# Set up I2C pins
i2c1_sda = Pin(14)
i2c1_scl = Pin(15)

# Set up I2C
i2c1 = I2C(1, sda=i2c1_sda, scl=i2c1_scl)

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)


ring = NeoPixel(Pin(2),12)

LEDdict={
    18:0,
    19:1,
    20:2,
    21:3,
    22:4,
    23:5,
    24:6,
    25:7,
    26:8,
    27:9,
    28:10,
    29:11 }

while True:
    temperature=round(dht20.measurements['t'])
    if temperature not in LEDdict:
        pass
        print("Out of temperature range")
    else:    
        LEDindex=(LEDdict[temperature])
        ring[LEDindex]= (10,0,0)
        ring.write()
        print(f"Temperature: {temperature}°C")
        time.sleep(10))
        time.sleep(10)