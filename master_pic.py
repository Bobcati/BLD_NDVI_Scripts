from picamera2 import Picamera2
import RPi.GPIO as GPIO
from time import sleep
from time import strftime
import keyboard
import os

# Camera Declaration
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (3280, 2464)})
picam2.configure(camera_config)
picam2.rotation = 180
picam2.start(show_preview=False)


#GPIO pin assignments (BCM labeling)
arduTrig = 17
zeroTrig = 14

#GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(arduTrig, GPIO.IN) # Input from ardupilot flight controller relay
GPIO.setup(zeroTrig, GPIO.OUT)

#Initial GPIO state
GPIO.output(zeroTrig, GPIO.LOW)

#Make new folder on boot
foldName = strftime("%d_%m_%y_at_%I_%M%p")
os.system("mkdir /home/bobcaticus/Tree_Analysis/Tree_Test_Pics/" + foldName)

def debounce():
    sleep(0.1)

def takePicture():
    picam2.capture_file("/home/bobcaticus/Tree_Analysis/Tree_Test_Pics/" + foldName + "/IR_" + strftime("%d_%m_%y_at_%I_%M%p_%S") + ".jpg")
    print("picture captured")

def triggerZero():
    GPIO.output(zeroTrig, GPIO.HIGH)

def resetZero():
    GPIO.output(zeroTrig, GPIO.LOW)

#Take pictures
while True:
    sleep(0.01)
    if GPIO.input(arduTrig):
        triggerZero()
        takePicture()
        sleep(0.1) # debounce so that camera is not triggered multiple times
        resetZero()  
    if keyboard.is_pressed("q"):
        print("Picture taking stopped")
        break

