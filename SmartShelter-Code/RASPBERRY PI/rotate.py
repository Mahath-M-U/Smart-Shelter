import RPi.GPIO as gpio
import time
from time import sleep
from main import *

def rotate1():
 init()
 gpio.output(5, True)
 gpio.output(6, False)
 sleep(1)
 gpio.cleanup()
def rotate2():
 init()
 gpio.output(5, False)
 gpio.output(6, True)
 sleep(1)
 gpio.cleanup()
 #set fire base

def rotate11():
 R = 0
 while True:
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)
  gpio.setup(10, gpio.IN) 
  i = gpio.input(10)
  if i == 1:
      print("i=",i)
      print("rotated")
      break
  if i != 1:
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(10, gpio.IN) 
    i= gpio.input(10)
    print("i=",i)#When output from gpio is high
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.output(5, True)
    gpio.output(6, False)
    gpio.cleanup()
    R=1
    print("rotaing")
    if i == 1:
        print("rotated")
        break
 while True:
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)
  gpio.setup(11, gpio.IN) 
  s = gpio.input(11)
  if s != 1:
      print("rotated")
      rotate1()
      print("s=",s)
      break
  if s == 0 and R == 0:#When output from gpio is low
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.output(5, False)
    gpio.output(6, True)
    gpio.cleanup()
    print("s=",s)
    print("reversing")
    if s == 1:
        print("rotated")
        rotate2()
        break
rotate1()
if __name__ == '__main__':
    try:
        rotate11()
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt by User")