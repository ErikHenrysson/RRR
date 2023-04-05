from fsm import *
from state import *
from controller import *
from mqtt_client import *
from data_manager import *

class vehicle(fsm):
    def __init__(self, mqtt_host:str, mqtt_port:int, mqtt_topic:str, gui):        
        self.state_list = [idle(), mobile(), recon(), terminate()]
        self.mqtt_client = mqtt_client(mqtt_host, mqtt_port, mqtt_topic)
        self.data_manager = data_manager(self.mqtt_client)
        self.gui = gui
        super().__init__(self.state_list)
        #self.run()

    #Run the vehicle with all the functionalities
    #TODO detta är inte klart, måste kollas över hur run method ska implementeras med ps4 kontroll.
    def run(self):
        current_state = self.get_current_state
        while(current_state != "terminate"):
            current_state = self.get_current_state()
            if current_state == "idle":
                pass
            elif current_state == "recon":
                self.save_data()
                self.gui.update()   
                #print("heartbeat")
            elif current_state == "mobile":
                pass

            '''
            Switch is not supported by python 3.9 
            match current_state:
                case "idle":
                    pass
                case "recon":
                    self.presenter.show()
                case "mobile":
                    pass
                case _:
                    pass
            '''
    
    def save_data(self):
        self.data_manager.save_data()