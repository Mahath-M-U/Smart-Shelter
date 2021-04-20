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
 sleep(sec)
 print("openig")
 gpio.cleanup()

def close(sec):
 init()
 gpio.output(13, True)
 gpio.output(19, False)
 sleep(sec)
 print("closing")
 gpio.cleanup()

def value():
    ch=0
def checkC():
 while True:
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)
  gpio.setup(2, gpio.IN) 
  i=gpio.input(2)
  if i == 1:                 #When output from motion sensor is LOW
     LEDOFF()
     print("closing",i)
  elif i == 0:
      firesetclose()
      firesetoff()
      gpio.cleanup()
      print("closed",i)
      break
def checkO():
 while True:
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)
  gpio.setup(3, gpio.IN) 
  i=gpio.input(3)
  if i == 1:                 #When output from motion sensor is LOW
     open(1)
     LEDON()
     print("opening",i)
  elif i == 0:
     firesetopen()
     fireseton()
     gpio.cleanup()
     print("opened",i)
     break
def LIcall():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'LIGHT')
 try:
     doc = doc_ref.get()
     LED=doc.to_dict()
     STATUS={'led_s': 'ON'}
     if LED == STATUS:
         print("ON")
         LEDON()
     elif LED != STATUS:
         print("OFF")
         LEDOFF()
 except google.cloud.exceptions.NotFound:
     print(u'No such document!')
def FRcall():
 doc_ref = db.collection(u'SMART-SHELTER').document(u'FLATFROM')
 try:
     doc = doc_ref.get()
     FLATFROM=doc.to_dict()
     STATUS={'flatform_value': 'STOP'}
     if FLATFROM == STATUS:
         print("STOPED")
     elif FLATFROM != STATUS:
         print("ROTATE")
         o=os.popen(" gnome-terminal -x python3 rotate.py").read()
         print(o)
 except google.cloud.exceptions.NotFound:
     print(u'No such document!')
def SHcall():
 value()
 ch=0
 doc_ref= db.collection(u'SMART-SHELTER').document(u'Shutter')
 try:
     doc = doc_ref.get()
     SHUTTER=doc.to_dict()
     STATUS={'Shutter_pos': 'open'}
     if SHUTTER == STATUS:
         print("OPEN")
         if ch == 1:
             checkO()
             ch=0
     elif SHUTTER != STATUS:
         print("CLOSE")
         if ch == 0:
             checkC()
             ch=1
 except google.cloud.exceptions.NotFound:
     print(u'No such document!')
def iotcall():
    doc_ref= db.collection(u'SMART-SHELTER').document(u'run')
    try:
        doc = doc_ref.get()
        SHUTTER=doc.to_dict()
        STATUS={'iot': 'on'}
        if SHUTTER == STATUS:
            SHcall()
            FRcall()
            LIcall()
        elif SHUTTER != STATUS:
            print("iotoff")
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')

if __name__ == '__main__':
    try:
        while True:
            iotcall()
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt by User")

    