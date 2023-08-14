from picamera2 import Picamera2
import RPi.GPIO as GPIO
from time import sleep
from time import strftime
import os

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1640, 1232)})
picam2.configure(camera_config)
picam2.rotation = 180
picam2.start(show_preview=False)

#Make new folder
foldName = strftime("%d_%m_%y_at_%I_%M%p")
os.system("mkdir /home/bobcaticus2/Tree_Analysis/Tree_Test_Pics/" + foldName)

#GPIO pin assignments (BCM labeling)
zeroTrig = 4

#GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(zeroTrig, GPIO.IN)

def debounce():
    sleep(0.1)

def takePicture():
    picam2.capture_file("/home/bobcaticus2/Tree_Analysis/Tree_Test_Pics/" + foldName + "/" + strftime("%d_%m_%y_at_%I_%M%p_%S") + ".jpg")
    print("picture captured")

while True:
    sleep(0.01)
    if GPIO.input(zeroTrig):
        takePicture() 
        sleep(0.05)