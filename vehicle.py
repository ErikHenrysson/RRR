#
from fsm import *
class vehicle(fsm):
    def __init__(self, state_list, motor_list, controller, presenter):
        super().__init__(state_list)
        self.motor_list = motor_list
        self.controller = controller
        self.presenter = presenter