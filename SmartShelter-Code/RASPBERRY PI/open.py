import RPi.GPIO as gpio
import time
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#servi
cred = credentials.Certificate('/home/pi/PRO/serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(13, gpio.OUT)
 gpio.setup(19, gpio.OUT)
 gpio.setup(26, gpio.OUT)

def open(sec):
 init()
 gpio.output(13, False)
 gpio.output(19, True)
 sleep(sec)
 print("openig")
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
 
def firesetopen():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'Shutter')
 doc_ref.set({
     u'Shutter_pos': u'open'
 })
 
def fireseton():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'LIGHT')
 doc_ref.set({
     u'led_s': u'ON'
 })
if __name__ == '__main__':
    try:
        while True:
            gpio.setwarnings(False)
            gpio.setmode(gpio.BCM)
            gpio.setup(3, gpio.IN) 
            i=gpio.input(3)
            if i == 1:                 #When output from motion sensor is LOW
                open(.1)
                LEDON()
                gpio.cleanup()
                print("opening",i)
            elif i == 0:
                firesetopen()
                fireseton()
                gpio.cleanup()
                print("opened",i)
                break
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("KeyboardInterrupt by User")
        gpio.cleanup()