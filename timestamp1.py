import picamera
from subprocess import call
from datetime import datetime
from time import sleep
import os
import subprocess
#our file path


while True:
        input=int(raw_input("Enter"))
        if input is 1:
                
                currenttime=datetime.now()
                filepath="/home/pi/Desktop/cookie/timestamp/"
                pictime=currenttime.strftime("%Y.%m.%d-%H%M%S")
                picname=pictime+'.jpg'
                completefilepath=filepath+picname
                
                with picamera.PiCamera() as camera:
                        camera.resolution=(1280,720)
                        camera.capture(completefilepath)
                print("We have taken a picture")
                timestampmsg=currenttime.strftime("%Y.%m.%d-%H%M%S")
                timestampcmd="/usr/bin/convert "+ completefilepath + " -pointsize 36 -fill red -annotate +700+650 ' " + timestampmsg +" ' "+completefilepath
                call([timestampcmd],shell=True)
                print "we hv timestamped our picture"
                #comd="python detect_barcode2_all.py --image download.jpg"
                #os.system("python p1.py")
                os.system("python detect_barcode2_all.py")
                #output = open( tmp_log_file, 'r' ).read()
                
                sleep(1)
        
	
