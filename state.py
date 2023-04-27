class state:
    '''
    State, encapsulates a name of a state and keeps track of its status.
    '''
    def __init__(self, name: str):
        '''
        Constructs a new 'state' object.

        :param name: String representation of the state.
        :return: Returns nothing.
        '''
        self.active = False
        self.name = name
        pass

    def activate(self):
        '''
        Function to activate the state.

        :return: Returns nothing.
        '''
        self.active = True

    def deactivate(self):
        '''
        Function to deactivate the state.

        :return: Returns nothing.
        '''
        self.active = False
        
    def get_status(self):
        '''
        Function to get the current status of the state.

        :return: Returns True if the state is active and False if not.
        '''
        return self.active
    
    def get_name(self):
        '''
        Function to retreive the name of the state.

        :return: Returns a string representation of the states name.
        '''
        return self.name
    
class idle(state):
    def __init__(self):
        super().__init__("idle")

class recon(state):
    def __init__(self):
        super().__init__("recon")

class mobile(state):
    def __init__(self):
        super().__init__("mobile")

class terminate(state):
    def __init__(self):
        super().__init__("terminate")
