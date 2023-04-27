from fsm import *
from state import *
from controller import *
from mqtt_client import *
from data_manager import *

class vehicle(fsm):
    '''
    vehicle encapsulates an mqtt-client and a gui.
    The class inherits from the 'fsm' class. 
    The class is used to controll the vehicle as a whole.
    '''
    def __init__(self, mqtt_host:str, mqtt_port:int, mqtt_topic:str, gui):        
        '''
        Constructs a new 'vehicle' object and runs it.

        :param mqtt_host: Specified mqtt broker.
        :param mqtt_port: Specified port.
        :param mqtt_topic: Topic to subscribe to.
        :param gui: Gui to show the data on.
        :return: Returns nothing.
        '''

        self.state_list = [idle(), mobile(), recon(), terminate()]
        self.mqtt_client = mqtt_client(mqtt_host, mqtt_port, mqtt_topic)
        self.data_manager = data_manager(self.mqtt_client)
        self.gui = gui
        super().__init__(self.state_list)
        #self.run()

    #Run the vehicle with all the functionalities
    #TODO detta är inte klart, måste kollas över hur run method ska implementeras med ps4 kontroll.
    def run(self):
        '''
        The run method keeps the vehicle object running until it is terminated.
        Different states does different things and can be added here.

        :return: Returns nothing.
        '''
        current_state = self.get_current_state
        while(current_state != "terminate"):
            current_state = self.get_current_state()
            if current_state == "idle":
                pass
            elif current_state == "recon":
                self.save_data()
                self.gui.update()   
            elif current_state == "mobile":
                pass
    
    def save_data(self):
        '''
        Function to call the data manegers loop.

        :return: Returns nothing.
        '''
        self.data_manager.save_data()