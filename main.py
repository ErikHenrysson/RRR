from state import *
from fsm import *
from controller import *
from mqtt_client import *
from presenter import *
#for debugging

idle_state = idle()
mobile_state = mobile()
recon_state = recon()

state_list = [idle_state, mobile_state, recon_state]

my_fsm = fsm(state_list=state_list)
my_controller = controller(my_fsm, "ps4")
my_mqtt_client = mqtt_client("192.168.4.1", 1883, "eazense/eazense_38FDFEB810B6/out")
my_presenter = presenter(my_mqtt_client)