import os
def iot():
 print("iot START")
 o=os.popen(" gnome-terminal -x python3 iotscan.py").read()
 print(o)
 print("iot STOP")
def rf():
 print("rfid START")
 o=os.popen(" gnome-terminal -x sudo python3 rfid.py").read()
 print(o)
 print("rfid STOP")
def face_de():
 print("face START")
 o=os.popen(" gnome-terminal -x python3 face.py").read()
 print(o)
 print("face STOP")
def em():
 print("em START")
 o=os.popen(" gnome-terminal -x sudo python3 EMER.py").read()
 print(o)
if __name__ == '__main__':
    try:
        iot()
        rf()
        face_de()
        em()
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt by User")