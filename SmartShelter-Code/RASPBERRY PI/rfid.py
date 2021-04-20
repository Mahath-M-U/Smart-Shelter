import serial
import os
import RPi.GPIO as gpio
import time
from time import sleep
def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(13, gpio.OUT)
 gpio.setup(19, gpio.OUT)
 gpio.setup(26, gpio.OUT)

def open(sec):
 init()
 gpio.output(13, False)
 gpio.output(19, True)
 print("openig")
 sleep(sec)
 gpio.cleanup()

def LEDON():
 init()
 gpio.output(26, True)
 print("done LED")
 gpio.cleanup()

def LEDOFF():
 init()
 gpio.output(26, False)
 print("done LEDOFF")
 gpio.cleanup()
def checkc():
        while True:
            gpio.setwarnings(False)
            gpio.setmode(gpio.BCM)
            gpio.setup(3, gpio.IN) 
            i=gpio.input(3)
            if i == 1:                 #When output from motion sensor is LOW
                open(.1)
                #LEDON()
                gpio.cleanup()
                print("opening",i)
            elif i == 0:
                break
if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
        while True:
            string = ser.read(12)
            if len(string) == 0:
                print("Please wave a tag")
            else:
                string = string[1:11]   # Strip header/trailer
                print(string)
                if string == b'0001705948':
                    checkc()
                    print("OPEN")
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt by User")

