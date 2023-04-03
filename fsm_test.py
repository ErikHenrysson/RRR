from state import *
from fsm import *
from controller import *
from mqtt_client import *
from presenter import *
from vehicle import *
#for debugging

my_vehicle = vehicle("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out")
my_vehicle.change_state("mobile")
my_vehicle.change_state("recon")
run = True
my_vehicle.run()
while(run):
    pass