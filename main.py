from state import *
from fsm import *
from controller import *
#for debugging

idle_state = idle()
mobile_state = mobile()
recon_state = recon()

state_list = [idle_state, mobile_state, recon_state]

myfsm = fsm(state_list=state_list)
mycontroller = controller(myfsm, "ps4")
myfsm.print_active_state()
mycontroller.cross_pressed()
myfsm.print_active_state()
mycontroller.circle_pressed()
myfsm.print_active_state()
mycontroller.triangle_pressed()
myfsm.print_active_state()
