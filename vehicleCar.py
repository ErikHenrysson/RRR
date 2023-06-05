from gpiozero import Servo, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from pyPS4Controller.controller import Controller
from multiprocessing import Process
import os, time
from fsm import *
from state import *
from vehicle import *
MR_FW = 17
MR_BW = 27
ML_FW = 23
ML_BW = 24
STEER_PIN = 18
STEER_MAX = (-0.8,0.8)
FWD_MAX = 1.0
BWD_MAX = 0.9
COLOURS = {"idle":[0,255,0],"playing":[255,50,100],"break":[255,0,0]}

def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax - outMin))

class MyController(Controller):
    def __init__(self, vehicle:vehicle, *args, **kwargs):
        Controller.__init__(self, *args, **kwargs)
        self.vehicle = vehicle
        #self.vehicle.change_state("recon")
        self.steering = Servo(STEER_PIN, pin_factory=PiGPIOFactory())
        self.ml_fw = PWMOutputDevice(ML_FW)
        self.ml_bw = PWMOutputDevice(ML_BW)
        self.mr_fw = PWMOutputDevice(MR_FW)
        self.mr_bw = PWMOutputDevice(MR_BW)
        self.set_led_colour(COLOURS["idle"])

    def set_led_colour(self, colour):
        # Use bash to set LED colour for right permissions 
        cmd = f"/home/pi/ExArb/RRR/leds.sh -r{colour[0]} -g{colour[1]} -b{colour[2]}"
        os.system(cmd)
    ''' 
    def on_circle_press(self):
        current_state = self.vehicle.get_current_state()
        self.set_led_colour(COLOURS["playing"])
        if current_state == "mobile":
            self.vehicle.change_state("idle")
    

        elif current_state == "idle":
            self.set_led_colour(COLOURS["break"])
            self.vehicle.change_state("recon")
    
    def on_square_press(self):
        current_state = self.vehicle.get_current_state()
        self.set_led_colour(COLOURS["idle"])

        if current_state == "recon":
            self.vehicle.change_state("idle")

        elif current_state == "idle":
            self.vehicle.change_state("mobile")
    '''        

    def on_R2_press(self, value):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.drive(value)

    def on_R2_release(self):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.halt()
        
    def on_L2_press(self, value):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.drive(value, False)

    def on_L2_release(self):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.halt()
        
    def on_x_press(self):
        current_state = self.vehicle.get_current_state()
        self.set_led_colour(COLOURS["break"])
        if current_state == "mobile":
            self.halt()
    
    def on_x_release(self):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.set_led_colour(COLOURS["idle"])
        
    def steer(self, value):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            value = num_to_range(value, -32767, 32767, STEER_MAX[0], STEER_MAX[1])
            self.steering.value = value
        
    def drive(self, value, fwd=True):
        max = FWD_MAX if fwd else BWD_MAX
        value = num_to_range(value, -32767, 32767, 0, max)
        if fwd:
            self.ml_bw.value = 0
            self.mr_bw.value = 0
            self.ml_fw.value = value
            self.mr_fw.value = value
        else:
            self.ml_fw.value = 0
            self.mr_fw.value = 0
            self.ml_bw.value = value
            self.mr_bw.value = value
            
    def halt(self):
        self.ml_fw.value = 0
        self.mr_fw.value = 0
        self.ml_bw.value = 0
        self.mr_bw.value = 0  
        time.sleep(0.1)
        self.set_led_colour(COLOURS["idle"])

    def on_L3_left(self, value):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.steer(-abs(value))

    def on_L3_right(self, value):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.steer(value)

    def on_L3_x_at_rest(self):
        current_state = self.vehicle.get_current_state()
        if current_state == "mobile":
            self.steer(0)


    
    def our_listen(self, vehicle:vehicle):
        self.vehicle = vehicle
        self.vehicle.change_state('mobile')
        self.listen()
        

def run_controller(vehicle:vehicle):
    controller = MyController(vehicle, interface="/dev/input/js0", connecting_using_ds4drv=False)
    print("före listen")
    controller.listen()
    print("efter listen")
    
'''  
if __name__ == '__main__':
    my_fsm = fsm([idle(), recon(), mobile()])
    p1 = Process(target=run_controller(my_fsm))
    p1.start()
    run = True
    while run:
        print("asd")
'''
