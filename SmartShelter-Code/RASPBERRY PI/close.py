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

def close(sec):
 init()
 gpio.output(13, True)
 gpio.output(19, False)
 sleep(sec)
 print("closing")
 gpio.cleanup()

def LEDOFF():
 init()
 gpio.output(26, False)
 print("done LEDOFF")
 gpio.cleanup()

def firesetclose():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'Shutter')
 doc_ref.set({
     u'Shutter_pos': u'close'
 })
def firesetoff():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'LIGHT')
 doc_ref.set({
     u'led_s': u'OFF'
 })
if __name__ == '__main__':
    try:
        while True:
            gpio.setwarnings(False)
            gpio.setmode(gpio.BCM)
            gpio.setup(2, gpio.IN) 
            i=gpio.input(2)
            if i == 1:                 #When output from motion sensor is LOW
                #close(4.25)
                close(.1)# Reset by pressing CTRL + C
                LEDOFF()
                gpio.cleanup()
                print("closing",i)
            elif i == 0:
                firesetclose()
                firesetoff()
                gpio.cleanup()
                print("closed",i)
                break
            
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt by User")