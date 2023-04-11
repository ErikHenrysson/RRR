from gpiozero import Servo
import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller
from multiprocessing import Process

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
    def __init__(self, *args, **kwargs):
        Controller.__init__(self, *args, **kwargs)
        GPIO.setup(OUT_PIN, GPIO.OUT)
        self.servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ)
        self.servo1.start(0)

    def on_R2_press(self, value):
        print("forward")
        GPIO.output(in1a, GPIO.HIGH)
        GPIO.output(in2a, GPIO.LOW)
        GPIO.output(in1b, GPIO.HIGH)
        GPIO.output(in2b, GPIO.LOW)

    def on_R2_release(self):
        GPIO.output(in1a, GPIO.LOW)
        GPIO.output(in2a, GPIO.LOW)
        GPIO.output(in1b, GPIO.LOW)
        GPIO.output(in2b, GPIO.LOW)

    def on_L2_press(self, value):
        print("backward")
        GPIO.output(in1a, GPIO.LOW)
        GPIO.output(in2a, GPIO.HIGH)
        GPIO.output(in1b, GPIO.LOW)
        GPIO.output(in2b, GPIO.HIGH)

    def on_L2_release(self):
        GPIO.output(in1a, GPIO.LOW)
        GPIO.output(in2a, GPIO.LOW)
        GPIO.output(in1b, GPIO.LOW)
        GPIO.output(in2b, GPIO.LOW)

    def on_L3_left(self, value):
        self.servo1.ChangeDutyCycle(2)

    def on_L3_right(self, value):
        self.servo1.ChangeDutyCycle(10)

    def on_L3_x_at_rest(self):
        self.servo1.ChangeDutyCycle(6.5)

    def on_R3_left(self, value):
        self.servo1.ChangeDutyCycle(2)

    def on_R3_right(self, value):
        self.servo1.ChangeDutyCycle(10)

    def on_R3_x_at_rest(self):
        self.servo1.ChangeDutyCycle(6.5)

def run_controller():
    print("Det är luungt123")
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    print("Det är luungt")
    controller.listen()
    print("Det är luungt")

def run_servo():
    while True:
        pass  # Add your servo code here
        print("Det är luungt2")

if __name__ == '__main__':
    p1 = Process(target=run_controller)
    p1.start()
    print("Det är luungt3")
    
