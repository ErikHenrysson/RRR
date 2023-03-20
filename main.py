from state import *
from fsm import *
from controller import *

idle_state = idle()
mobile_state = mobile()
recon_state = recon()
state_list = [idle_state, mobile_state, recon_state]

myfsm = fsm(state_list=state_list)
mycontroller = controller(myfsm, "ps4")
mycontroller.cross_pressed()
mycontroller.circle_pressed()
mycontroller.triangle_pressed()
