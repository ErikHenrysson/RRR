from state import *
class fsm:
    '''
    Finite state machine. Encapsulates a list of allowed states. 
    '''
    def __init__(self, state_list: list):
        '''
        Constructs a new 'fsm' object.

        :param state_list: A list of allowed states
        :return: Returns nothing.
        '''
        self.state_list = state_list
        self.current_state = "idle"
        self.change_state("idle")

    def change_state(self, new_state: str):
        '''
        Deactivate the current state and activate the specified one.

        :param new_state: Desired state
        :return: Returns nothing.
        '''
        #Search through states to find current one, deactivate it, activate the new
        for state in self.state_list:
            if state.get_name() == self.current_state:
                state.deactivate()
            if state.get_name() == new_state:
                state.activate()

        print("state:", self.current_state, "changed to:", new_state)
        self.current_state = new_state

    def get_current_state(self):
        '''
        Returns the currently activated state.

        :return: Returns a string representation of the currently activated state.
        '''
        return self.current_state
    

    def print_active_state(self):
        '''
        Prints the currently activated state to the console.

        :return: Returns nothing.
        '''
        for state in self.state_list:
            print(state.get_name(), "status:", state.get_status())