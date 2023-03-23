#Tanken med presenter är att den får färdig information som den kan presentera med förslagsvis matplotlib
from receiver import *
from mqtt_client import *
class presenter:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client


    def show(self):
        if self.mqtt_client.new_available_message():
            #if the client has new message, read the new message
            message = self.mqtt_client.read_message()
            self.draw(message)

    #extract useful information and draw the information with matplotlib?
    def draw(self, message):
        pass

    #Extracts the desired parameters from the mqtt json message
    def extract_json(self, desired_params):
        pass
    
    #should be called regurarely
    def loop_mqtt(self):
        self.mqtt_client.my_loop()

#mymqttclient = MqttClient("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out")
#print("Made iot past the creation of the mqttclient")
#mypresenter = presenter(mymqttclient)
#counter = 0
#while(1==1):
#    if counter == 1000:
#        mypresenter.loop_mqtt()
#    counter=counter+1
#    pass