from state import *
from fsm import *
#from controller import *
from mqtt_client import *
from data_manager import *
from vehicle import *
from gui import *
from multiprocessing import Process
from vehicleCar import *


my_gui = gui()

my_vehicle = vehicle("192.168.4.1", 1883, "eazense/eazense_38FDFEB810B5/out", my_gui)
my_vehicle.change_state("recon")
#Skapa kontrollen
my_controller = MyController(my_vehicle, interface="/dev/input/js0", connecting_using_ds4drv=False)
#gör listen() som process istället
print("efter mycontroller")
p1 = Process(target = my_controller.our_listen, args=(my_vehicle,))
#p1 = Process(target=run_controller,args= (my_vehicle,))
print("före start1 i main")
p1.start()
print("efter start1 i main")
my_vehicle.run()
#p2 = Process(target=my_vehicle.run)
#p2.start()
print("efter start2 i main")
