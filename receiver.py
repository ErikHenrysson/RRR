#Class for receiving mqtt packages
#Has a list of all the mqtt_clients
#when recquested, check new mqtt messages and return to correct "subscriber"
from mqtt_client import *

class receiver:
    def __init__(self, mqtt_client_list: list):
        self.mqtt_client_list = mqtt_client_list

    def check_new_messsages(self):
        for mqtt_client in self.mqtt_client_list:
            if mqtt_client.new_available_message():
                #if the targeted mqtt_client has an available message, do what?
                message = mqtt_client.read_message()

