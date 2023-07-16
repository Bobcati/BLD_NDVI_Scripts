'''
This program takes pictures on the raspberry pi every time the GPIO is triggered.
'''
from picamera2 import Picamera2
import RPi.GPIO as GPIO
from time import sleep
from time import strftime

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (3280, 2464)})
picam2.configure(camera_config)
picam2.start(show_preview=False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def debounce():
    sleep(0.06)

def takePicture():
    print("picture captured")
    picam2.start_and_capture_file("/home/pi/Tree_Analysis/Plant_Test_Pics/" + strftime("%d/%m/%y at %I:%M%p:%S:%f") + ".jpg")

while True:
    time.sleep(0.01)
    if GPIO.input(23):
        takePicture()
        debounce()
