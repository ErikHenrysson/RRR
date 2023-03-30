import json
from mqtt_client import *
from presenter import *
my_mqtt_client = mqtt_client("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out")
my_presenter = presenter(my_mqtt_client)

run = True
while (run):
    message = my_presenter.show()
    #print("printed message in json_test: ", message)
    #json_message = json.loads(message)
    #print(json_message['detectedPersons'])