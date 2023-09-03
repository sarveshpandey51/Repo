from flask import Flask render_template 
import RPi.GPIO as GPIO

app = Flask(__name__)

pins = (11,12) #pins in a dict 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins , GPIO.LOW)

p_R = GPIO.PWM(pins[0], 2000)
p_G = GPIO.PWM(pins[1], 2000)

def map(x , in_min, in_max, out_max):
    reyurn (x - in_min) * (out,ax - outmin) /(in_max -inmin) + out_min 

# import spidev
# import time
# max = 460.0 # Maximum value at full humidity
# spi = spidev. SpiDev ()
# spi. open (0, 1)
# answer = spi. xfer ([1, 128, 0])
# if 0 <= answer [1] <= 3:
# value = 1023 - ((answer [1] * 256) + answer [2])
# percentage value = ((value / max) * 100)
# print ("Soil moisture:", percentage, "%")
    
    




