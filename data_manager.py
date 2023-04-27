#Tanken med presenter är att den får färdig information som den kan presentera med förslagsvis matplotlib
from receiver import *
from mqtt_client import *
import paho.mqtt.client as mqtt
import json
from my_target import *
from math import sqrt, pi, acos
import numpy as np
import matplotlib.pyplot as plt
from public_func import *
class data_manager:
    '''
    The data manager fetches data from the MQTT client. When it receives new data, it extracts the relevant information
    about the targets and keeps track of them in a list. 

    The data manager has two modes, multi or single target detection.
    '''
    def __init__(self, mqtt_client: mqtt_client):
        '''
        Constructs a new 'data_manager' object.
        
        :param mqtt_client: Specified mqtt client to extract data from
        :return: Returns nothing
        '''
        self.mqtt_client = mqtt_client
        self.targets:list[my_target] = []
        self.new_targets:list[my_target] = []
        self.id:int = 0
        self.threshold = 1
        self.multiple = False

    #TODO behöver den returnera en string? kanske ta bort
    def save_data(self) -> str:
        '''
        Checks if there is a new data package from the mqtt client. If there is, it extracts the targets from the package.
        If multi target detection is enabled, it compares old and new targets and keeps track of them.

        :return: returns nothing??
        '''
        self.mqtt_client.my_loop()
        if self.mqtt_client.new_available_message():
            #if the client has new message, read the new message
            self.message = self.mqtt_client.read_message()
            #print(self.message)
            #Extract the targets and remove duplicates
            if self.multiple:
                self.extract_json(self.message)
                with open('radarData.txt', 'w') as f:
                    for target in self.targets:
                        lines = [str(target.get_x()),
                                ',',
                                str(target.get_y()),
                                ',',
                                str(target.get_z()),
                                ',',
                                str(target.get_vel()),
                                ',',
                                str(target.get_old_angle()),
                                ',',
                                str(target.get_old_r()),
                                '\n']
                        f.writelines(lines)
            else:
                self.extract_single_json(self.message)
                with open('radarData.txt', 'w') as f:
                    for target in self.targets:
                        lines = [str(target.get_x()),
                                ',',
                                str(target.get_y()),
                                ',',
                                str(target.get_z()),
                                ',',
                                str(target.get_vel()),
                                ',',
                                str(target.get_old_angle()),
                                ',',
                                str(target.get_old_r()),
                                '\n']
                        f.writelines(lines)

    #Extracts the desired parameters from the mqtt json message
    #Creates new targets that can be comprade with old ones to see if they are new or not
    #TODO behöver den returnera en lista??
    def extract_json(self, message) -> list:
        '''
        Extracts the useful information from the JSON package from the mqtt client. 
        When the information is extracted and saved, it is compared to the list of saved targets.
        Can extract and compare multiple targets.

        :param message: The JSON message to be analyzed
        :return: Returns nothing ??
        '''
        json_message = json.loads(message)
        created_time = int(json_message['createdTime'])
        detected_targets = json_message['detectedPersons']
        num_targets = detected_targets['noOfPerson']
        if num_targets != 0:
            for target in detected_targets['persons']:
                target = my_target(x=float(target['x']),y=float(target['y']),z=float(target['z']),vel=float(target['activity']), id=self.id, created_time=created_time)
                target.print_target()
                self.id += 1
                is_new_target = self.compare_new_target(target)
                if not is_new_target:
                    self.id -=1
    
    def compare_new_target(self, new_target:my_target) -> bool:
        '''
        Compares a new target to the list of current ones. If the distance from the new targets is within the desired range 
        of the old ones (the old targets velocity is taken into account) it is considered an old target which have moved.

        :param new_target: The new target which should be compared to the current targets.
        :return: Returns True if new_target is considered a new target. Returns False if new_target is considered a previously recorded one.
        '''
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
                time_diff = new_target.get_created_time() - target.get_created_time()
                print("distance in compare_new_target:", distance)
                #TODO figure out what the threshold should be? Time * velocity + some leaway?
                if distance <= time_diff*target.get_vel() + 1:
                    angle, dist = extract_angle_and_dist(x1,y1)
                    target.set_old_angle(angle)
                    target.set_old_r(dist)
                    target.set_x(new_target.get_x())
                    target.set_y(new_target.get_y())
                    target.set_z(new_target.get_z())
                    target.set_vel(new_target.get_vel())
                    return False
                else:
                    #if it is a new target, return true and add it to the new target list 
                    self.targets.append(new_target)
                    return True 
        else:
            #if the list of targets is empty, we know its a new target so add it to the list and return true
            self.targets.append(new_target)
            return True



    #TODO If there is multiple targets in the package, save the one that is closest to the saved one. Does it need a return??
    def extract_single_json(self, message) -> list:
        '''
        Extracts the useful information from the JSON package from the mqtt client. Updates the saved targets location.
        Used when single target detection is enabled. The target closest to the 

        :param message: The JSON message to be analyzed.
        :return: Returns nothing ????
        '''
        json_message = json.loads(message)
        created_time = int(json_message['createdTime'])
        detected_targets = json_message['detectedPersons']
        num_targets = detected_targets['noOfPerson']
        if num_targets != 0:
            for target in detected_targets['persons']:
                target = my_target(x=float(target['x']),y=float(target['y']),z=float(target['z']),vel=float(target['activity']), id=self.id, created_time=created_time)
                target.print_target()
                self.id += 1
                is_new_target = self.compare_single(target)
                if not is_new_target:
                    self.id -=1
                return

                
    def compare_single(self, new_target:my_target):
        '''
        Updates the saved target with the new one. Adds the old coordinates for representation in the gui class.

        :param new_target: The new target which should replace the old one
        :return: Returns nothing.
        '''
        if (self.targets):
            old_target = self.targets[0]
            old_angle, old_r = extract_angle_and_dist(old_target.get_x(), old_target.get_y())
            new_target.set_old_angle(old_angle)
            new_target.set_old_r(old_r)
        self.targets.clear()
        self.targets.append(new_target)

    def loop_mqtt(self):
        '''
        Tells the mqtt client to run its loop.
        '''
        self.mqtt_client.my_loop()
