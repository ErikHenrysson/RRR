#Snabb draft

class fsm:
    def __init__(self, state_list):
        self.state_list = state_list
        self.current_state = "idle"

    
    def change_state(self, state):
        print("State changed to:", state)
        self.current_state = state

    