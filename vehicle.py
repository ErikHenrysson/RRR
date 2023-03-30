from fsm import *
from state import *
from controller import *
from mqtt_client import *
from presenter import *

class vehicle(fsm):
    def __init__(self):        
        idle_state = idle()
        mobile_state = mobile()
        recon_state = recon()
        terminate_state = terminate()
        self.state_list = [idle_state, mobile_state, recon_state, terminate_state]

        self.mqtt_client = mqtt_client("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out")
        self.presenter = presenter(self.mqtt_client)
        
        super().__init__(self.state_list)
        self.change_state("recon")
        self.run()
        #self.motor_list = motor_list
        #self.controller = controller
        #self.controller = controller(self.fsm, "ps4")

    #Run the vehicle with all the functionalities
    #TODO detta är inte klart, måste kollas över hur run method ska implementeras med ps4 kontroll
    def run(self):
        current_state = self.get_current_state
        while(current_state != "terminate"):
            current_state = self.get_current_state()
            match current_state:
                case "idle":
                    pass
                case "recon":
                    self.presenter.show()
                case "mobile":
                    pass
                case _:
                    pass
