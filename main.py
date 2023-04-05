from state import *
from fsm import *
from controller import *
from mqtt_client import *
from data_manager import *
from vehicle import *
from gui import *
#for debugging


gui = SeaofBTCapp()
my_vehicle = vehicle("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out", gui)
my_vehicle.change_state("mobile")
my_vehicle.change_state("recon")
my_vehicle.run()
