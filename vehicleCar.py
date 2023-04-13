from gpiozero import Servo
import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller
from multiprocessing import Process
from fsm import *
from state import *

GPIO.setmode(GPIO.BOARD)

in1a = 16
in2a = 18
ena = 32

in1b = 11
in2b = 13
enb = 33

OUT_PIN = 36
PULSE_FREQ = 50

# Motor 1 Right Setup
GPIO.setup(in1a, GPIO.OUT)
GPIO.setup(in2a, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)
PWMA = GPIO.PWM(ena, 100)
PWMA.start(0)

# Motor 2 Left Setup
GPIO.setup(in1b, GPIO.OUT)
GPIO.setup(in2b, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
PWMB = GPIO.PWM(enb, 100)
PWMB.start(0)

class MyController(Controller):
    def __init__(self, fsm:fsm, *args, **kwargs):
        Controller.__init__(self, *args, **kwargs)
        self.fsm = fsm
        GPIO.setup(OUT_PIN, GPIO.OUT)
        self.servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ)
        self.servo1.start(0)
        
    def on_circle_press(self):
        current_state = self.fsm.get_current_state()
        
        if current_state == "mobile":
            self.fsm.change_state("idle")
    

        elif current_state == "idle":
            self.fsm.change_state("recon")
        
            
    
    def on_square_press(self):
        current_state = self.fsm.get_current_state()

        if current_state == "recon":
            self.fsm.change_state("idle")

        elif current_state == "idle":
            self.fsm.change_state("mobile")


    def on_R2_press(self, value):
        current_state = self.fsm.get_current_state()
        if current_state == "mobile":
            print("forward")
            GPIO.output(in1a, GPIO.HIGH)
            GPIO.output(in2a, GPIO.LOW)
            GPIO.output(in1b, GPIO.HIGH)
            GPIO.output(in2b, GPIO.LOW)

    def on_R2_release(self):
        current_state = self.fsm.get_current_state()
        if current_state == "mobile":
            GPIO.output(in1a, GPIO.LOW)
            GPIO.output(in2a, GPIO.LOW)
            GPIO.output(in1b, GPIO.LOW)
            GPIO.output(in2b, GPIO.LOW)

    def on_L2_press(self, value):
        current_state = self.fsm.get_current_state()
        if current_state == "mobile":
            print("backward")
            GPIO.output(in1a, GPIO.LOW)
            GPIO.output(in2a, GPIO.HIGH)
            GPIO.output(in1b, GPIO.LOW)
            GPIO.output(in2b, GPIO.HIGH)

    def on_L2_release(self):
        current_state = self.fsm.get_current_state()
        if current_state == "mobile":
            GPIO.output(in1a, GPIO.LOW)
            GPIO.output(in2a, GPIO.LOW)
            GPIO.output(in1b, GPIO.LOW)
            GPIO.output(in2b, GPIO.LOW)

    def on_L3_left(self, value):
        current_state = self.fsm.get_current_state()
        if current_state == "mobile":
            self.servo1.ChangeDutyCycle(2)

    def on_L3_right(self, value):
        current_state = self.fsm.get_current_state()
        if current_state == "mobile":
            self.servo1.ChangeDutyCycle(10)

    def on_L3_x_at_rest(self):
        current_state = self.fsm.get_current_state()
        if current_state == "mobile":
            self.servo1.ChangeDutyCycle(6.5)

    #def on_R3_left(self, value):
    #    self.servo1.ChangeDutyCycle(2)

   # def on_R3_right(self, value):
   #     self.servo1.ChangeDutyCycle(10)

   # def on_R3_x_at_rest(self):
   #     self.servo1.ChangeDutyCycle(6.5)
        
        
    


def run_controller(fsm:fsm):
    print("Det är luungt123")
    controller = MyController(fsm, interface="/dev/input/js0", connecting_using_ds4drv=False)
    print("Det är luungt")
    controller.listen()
    print("Det är luungt")

def run_servo():
    while True:
        pass  # Add your servo code here

if __name__ == '__main__':
    my_fsm = fsm([idle(), recon(), mobile()])
    p1 = Process(target=run_controller(my_fsm))
    p1.start()
    run = True
    while run:
        pass
        #print("lungan")
