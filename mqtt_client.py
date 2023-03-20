#Hämtar json packeten som radarn skickar ut
#kanske ska kunna publisha mqtt till radarn också för att configurera?
import paho.mqtt.client as mqtt
class MqttClient:
    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic
        self.last_message = ""              
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.get_host(), self.get_port(), 60)

        client.loop_forever()

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
        print(msg.topic+" "+str(msg.payload))

    def start(self):
        pass

mymqttclient = MqttClient("test.mosquitto.org", 1883, "eazense/eazense_38FDFEB810B6/out")
mymqttclient.start()
#TODO change loop forever to something threadable
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
