from gpiozero import Servo
import RPi.GPIO as GPIO          
from time import sleep
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

in1a = 16
in2a= 18
ena = 32

in1b = 11
in2b = 13
enb = 33

OUT_PIN = 36
PULSE_FREQ = 50

#Motor 1 Right Setup
GPIO.setup(in1a,GPIO.OUT)
GPIO.setup(in2a,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
PWMA = GPIO.PWM(ena,100)
PWMA.start(0)

# Motor 2 Left Setup
GPIO.setup(in1b,GPIO.OUT)
GPIO.setup(in2b,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
PWMB = GPIO.PWM(enb,100)
PWMB.start(0)

# Servo Setup
GPIO.setup(OUT_PIN, GPIO.OUT) 
servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

servo1.start(0)
        
class MyController(Controller):
    print("test")

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_R2_press(self, value):
        print("forward")
        GPIO.output(in1a,GPIO.HIGH)
        GPIO.output(in2a,GPIO.LOW)
        GPIO.output(in1b,GPIO.HIGH)
        GPIO.output(in2b,GPIO.LOW)
        temp1=1

        
    def on_R2_release(self):
        GPIO.output(in1a,GPIO.LOW)
        GPIO.output(in2a,GPIO.LOW)
        GPIO.output(in1b,GPIO.LOW)
        GPIO.output(in2b,GPIO.LOW)

        
        
    def on_L2_press(self, value):
        print("backward")
        GPIO.output(in1a,GPIO.LOW)
        GPIO.output(in2a,GPIO.HIGH)
        GPIO.output(in1b,GPIO.LOW)
        GPIO.output(in2b,GPIO.HIGH)
        temp1=0

        
    
    def on_L2_release(self):
        GPIO.output(in1a,GPIO.LOW)
        GPIO.output(in2a,GPIO.LOW)
        GPIO.output(in1b,GPIO.LOW)
        GPIO.output(in2b,GPIO.LOW)
        
        
    def on_L3_left(self, value):
        servo1.ChangeDutyCycle(2)


    def on_L3_right(self, value):
        servo1.ChangeDutyCycle(10)
        
        
    def on_L3_x_at_rest(self):
        servo1.ChangeDutyCycle(6.5)
        
    def on_R3_left(self, value):
        servo1.ChangeDutyCycle(2)

  
    def on_R3_right(self, value):
        servo1.ChangeDutyCycle(10)
        
        
    def on_R3_x_at_rest(self):
        servo1.ChangeDutyCycle(6.5)
        
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#Något sånt här
#run = True
#while run:
        #controller.read()
        #print("jag kom förbi")
#TODO försök byta ut listen() mot något som bara läser när man kallar på funktionen
controller.listen()
