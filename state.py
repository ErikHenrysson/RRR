#Tanke med detta:
#Skapa ett interface som heter state
#Varje state skapar sina egna actions
#Används i konstruktorn för finite state machinen (fsm.py) för att kontrollera roboten
class state:
    def __init__(self):
        pass

#Alla states ärver från parent-klassen "state"
class idle(state):
    def __init__(self):
        super().__init__()

class recon(state):
    def __init__(self):
        super().__init__()

class mobile(state):
    def __init__(self):
        super().__init__()
