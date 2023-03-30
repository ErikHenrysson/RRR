#Tanke med detta:
#Skapa ett interface som heter state
#Varje state skapar sina egna actions
#Används i konstruktorn för finite state machinen (fsm.py) för att kontrollera roboten
class state:
    def __init__(self, name: str):
        self.active = False
        self.name = name
        pass

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False
        
    def get_status(self):
        return self.active
    
    def get_name(self):
        return self.name
    
#Alla states ärver från parent-klassen "state"
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
