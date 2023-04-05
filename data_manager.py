#Tanken med presenter är att den får färdig information som den kan presentera med förslagsvis matplotlib
from receiver import *
from mqtt_client import *
import paho.mqtt.client as mqtt
import json
from my_target import *
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

class data_manager:
    def __init__(self, mqtt_client: mqtt_client):
        self.mqtt_client = mqtt_client
        self.targets:list[my_target] = []
        self.new_targets:list[my_target] = []
        self.id:int = 0
        self.threshold = 1


    def save_data(self) -> str:
        self.mqtt_client.my_loop()
        if self.mqtt_client.new_available_message():
            #if the client has new message, read the new message
            self.message = self.mqtt_client.read_message()
            #print(self.message)
            #Extract the targets and remove duplicates
            self.extract_json(self.message)
            with open('radarData.txt', 'w') as f:
                for target in self.targets:
                    lines = [str(target.get_x()), ',',str(target.get_y()),',', str(target.get_z()),',',str(target.get_vel()),'\n']
                    f.writelines(lines)

    #Extracts the desired parameters from the mqtt json message
    #Creates new targets that can be comprade with old ones to see if they are new or not
    def extract_json(self, message) -> list:
        #for testing
        json_message = json.loads(message)
        detected_targets = json_message['detectedPersons']
        num_targets = detected_targets['noOfPerson']
        if num_targets != 0:
            for target in detected_targets['persons']:
                target = my_target(float(target['x']),float(target['y']),float(target['z']),float(target['activity']), self.id)
                self.id += 1
                is_new_target = self.compare_new_target(target)
                if not is_new_target:
                    self.id -=1
    
    # Maybe its better to compare a single target each time it is created, easier to keep track of target ids that way.
    def compare_new_target(self, new_target:my_target) -> bool:
        if bool(self.targets):
            for target in self.targets:
                target.print_target()
                x1:float = target.get_x()
                x2:float = new_target.get_x()
                y1:float = target.get_y()
                y2:float = new_target.get_y()
                z1:float = target.get_z()
                z2:float = new_target.get_z()
                #pythagoras to get distance between two points in 3d room
                distance = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))
                print(distance)
                #if it is the same target, update the old targets information
                if distance <= self.threshold:
                    target.set_x(new_target.get_x)
                    target.set_y(new_target.get_y)
                    target.set_z(new_target.get_z)
                    target.set_vel(new_target.get_vel)
                    
                    return False
                else:
                    #if it is a new target, return true and add it to the new target list 
                    self.targets.append(new_target)
                    return True 
        else:
            #if the list of targets is empty, we know its a new target so add it to the list and return true
            self.targets.append(new_target)
            return True

    #should be called regurarely
    def loop_mqtt(self):
        self.mqtt_client.my_loop()


    '''
    #for each pair of targets, check if they are close enough to each other that they probably are the same target
    #should be able to set a threshhold for this value
    #TODO decide how to compare the different targets to determine if they are the same or not and figure out if this one is better than the single one
    def compare_new_targets(self):
        if bool(self.targets) & bool(self.new_targets):
            for target in self.targets:
                for new_target in self.new_targets:
                    x1:float = target.get_x()
                    x2:float = new_target.get_x()
                    y1:float = target.get_y()
                    y2:float = new_target.get_y()
                    z1:float = target.get_z()
                    z2:float = new_target.get_z()
                    #pythagoras to get distance between two points in 3d room
                    distance = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))
                    #distance = sqrt((target.get_x-new_target.get_x)*(target.get_x-new_target.get_x) + \
                    #    (target.get_y-new_target.get_y)*(target.get_y - new_target.get_y) + \
                    #    (target.get_z-new_target.get_z)*(target.get_z - new_target.get_z))
                    #if its lower than the threshold, the new_target is not considered "a new target" -> remove it from the new targets list
                    print(distance)
                    if distance <= self.threshold:
                        self.new_targets.remove(new_target)

            while(bool(self.new_targets)):
                self.targets.append(self.new_targets.pop())    

        '''



#mymqttclient = MqttClient("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out")
#print("Made iot past the creation of the mqttclient")
#mypresenter = presenter(mymqttclient)
#counter = 0
#while(1==1):
#    if counter == 1000:
#        mypresenter.loop_mqtt()
#    counter=counter+1
#    pass