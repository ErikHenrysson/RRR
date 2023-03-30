#Snabb draft
from state import *
class fsm:
    def __init__(self, state_list: list):
        self.state_list = state_list
        self.current_state = "idle"
        self.change_state("idle")

    #TODO Possible to increase efficiency by handling the edge case of activating the current state when booting, could make the for loop to if and else if instead of double if
    def change_state(self, new_state: str):
        #Search through states to find current one, deactivate it, activate the new
        for state in self.state_list:
            if state.get_name() == self.current_state:
                state.deactivate()
            if state.get_name() == new_state:
                state.activate()

        print("state:", self.current_state, "changed to:", new_state)
        self.current_state = new_state

    def get_current_state(self):
        return self.current_state
    

    def print_active_state(self):
        for state in self.state_list:
            print(state.get_name(), "status:", state.get_status())