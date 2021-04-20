from main import *
import RPi.GPIO as gpio
def checks():
 gpio.setwarnings(False)
 gpio.setmode(gpio.BCM)
 gpio.setup(8, gpio.IN) 
 i=gpio.input(8)
 print(gpio.input(8))
 while i == 0:                 #When output from motion sensor is LOW
    open(1)
    LEDON2()
    print("run")
 firesetopen()
 fireseton()
 gpio.cleanup()
checks()
sleep(5)
LEDOFF2()