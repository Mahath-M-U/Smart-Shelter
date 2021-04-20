import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
def mails():
 #frame = cv2.VideoCapture(0)
 #for i in range(2):
 #   cv2.imwrite('unKnown'+str(i)+'.png', image)
 #del(frame)
 #o=os.popen('scrot /home/pi/PRO/unKnown0.png').read()
 #print(o)
 
 email_user = 'mmu03091997@gmail.com'
 email_password = 'Qwertyuiop@1'
 email_send = 'mahathmundakkal@gmail.com'
 subject = 'subject'
 msg = MIMEMultipart()
 msg['From'] = email_user
 msg['To'] = email_send
 msg['Subject'] = subject
 body = 'AN UNKNOWN FACE DECTECT'
 msg.attach(MIMEText(body,'plain'))
 filename='unKnown0.png'
 attachment  =open(filename,'rb')
 part = MIMEBase('application','octet-stream')
 part.set_payload((attachment).read())
 encoders.encode_base64(part)
 part.add_header('Content-Disposition',"attachment; filename= "+filename)
 msg.attach(part)
 text = msg.as_string()
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login(email_user,email_password)
 server.sendmail(email_user,email_send,text)
 server.quit()
if __name__ == '__main__':
    try:
        mails()
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt by User")