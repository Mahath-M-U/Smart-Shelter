import RPi.GPIO as gpio
import time
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

#servi
cred = credentials.Certificate('/home/pi/PRO/serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(26, gpio.OUT)
 gpio.setup(16, gpio.OUT)
 gpio.setup(5, gpio.OUT)
 gpio.setup(6, gpio.OUT)
 gpio.setup(25, gpio.OUT)
 
def LEDON():
 init()
 gpio.output(26, True)
 print("done LED")
 time.sleep(1)
 gpio.cleanup()

def LEDOFF():
 init()
 gpio.output(26, False)
 print("done LEDOFF")
 time.sleep(1)
 gpio.cleanup()

def LEDON2():
 init()
 gpio.output(25, True)
 time.sleep(1)
 gpio.cleanup()

def LEDOFF2():
 init()
 gpio.output(25, False)
 time.sleep(1)
 gpio.cleanup()

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
def fireseton():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'LIGHT')
 doc_ref.set({
     u'led_s': u'ON'
 })
def firesetoff():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'LIGHT')
 doc_ref.set({
     u'led_s': u'OFF'
 })
def firesetopen():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'Shutter')
 doc_ref.set({
     u'Shutter_pos': u'open'
 })
def firesetclose():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'Shutter')
 doc_ref.set({
     u'Shutter_pos': u'close'
 })
#pir
def closed():
 o=os.popen(" gnome-terminal -x python3 close.py").read()
 print(o)

def pir(sec):
 g=0
 while True:
     gpio.setwarnings(False)
     gpio.setmode(gpio.BCM)
     gpio.setup(23, gpio.IN)
     sleep(4)
     i=gpio.input(23)
     if i== 0:
         if g ==0:#When output from motion sensor is LOW
             print("Intruder not detected",i)
             sleep(1)
             close(1)
         g=0
     elif i == 1:               #When output from motion sensor is HIGH
         print ("Intruder detected", i)
         g=0
         gpio.cleanup()
         sleep(2)
if __name__ == '__main__':
    try:
        print("imported Main")
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("KeyboardInterrupt by User")
        gpio.cleanup()
    