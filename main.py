from state import *
from fsm import *
from controller import *
from mqtt_client import *
from data_manager import *
from vehicle import *
from gui import *
#for debugging


my_gui = gui()
#run = True
#while run:
#    gui.update()
my_vehicle = vehicle("192.168.4.1", 1883, "eazense/eazense_38FDFEB810B6/out",my_gui)
my_vehicle.change_state("mobile")
my_vehicle.change_state("recon")
my_vehicle.run()
