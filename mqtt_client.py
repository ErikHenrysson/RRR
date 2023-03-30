#Hämtar json packeten som radarn skickar ut
#kanske ska kunna publisha mqtt till radarn också för att configurera?
import paho.mqtt.client as mqtt
class mqtt_client:
    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic
        self.last_message = ""
        self.new_message = False              
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.get_host(), self.get_port(), 60)
    def get_host(self):
        return self.host
    def get_port(self):
        return self.port
    def get_topic(self):
        return self.topic

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.get_topic())

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        self.new_message = True
        self.last_message = (msg.topic+" "+str(msg.payload))

    def new_available_message(self):
        return self.new_message
    
    def read_message(self):
        self.new_message = False
        return self.last_message
    
    def my_loop(self):
        self.client.loop()

#Test
#mymqttclient = MqttClient("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out")
#run = True
#counter = 0
#while(run):
#    counter+=1
#    if (counter%1000 == 0):
#        print("heartbeat")
#        mymqttclient.my_loop()
#TODO change loop forever to something threadable
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
