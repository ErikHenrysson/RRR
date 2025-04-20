#Hämtar json packeten som radarn skickar ut
#kanske ska kunna publisha mqtt till radarn också för att configurera?
import paho.mqtt.client as mqtt
import json
class mqtt_client:
    '''
    mqtt_client is a MQTT client subscriber.
    '''
    def __init__(self, host: str, port: int, topic: str):
        '''
        Constructs a new 'mqtt_client' object.

        :param host: String representation of the host.
        :param port: Port number.
        :param topic: Topic to subscribe to.
        '''
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
        '''
        Returns the host name.

        :return: Returns the host name.
        '''
        return self.host

    def get_port(self):
        '''
        Returns the port number.

        :return: Returns the port number.
        '''
        return self.port
    def get_topic(self):
        '''
        Returns the topic.

        :return: Returns the topic that the client is subscribed to.
        '''
        return self.topic

    def on_connect(self, client, userdata, flags, rc):
        '''
        The callback function for when the client receives a connection accepted response from the server.

        :return: Returns nothing.
        '''
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.get_topic())

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        '''
        The callback function for when something is published to the subscribed topic.

        :return: Returns nothing
        '''
        decoded_message=str(msg.payload.decode("utf-8"))
        if decoded_message != "":
            json_message=json.loads(decoded_message)
            self.last_message = json.dumps(json_message, indent=2)
            self.new_message = True
        
    def new_available_message(self):
        '''
        Function to let other objects know if it has a new message.

        :return: Returns True if it has a new message and False if it doesn't.
        '''
        return self.new_message
    
    def read_message(self):
        '''
        Reads the most current message and sets the new_message flag to False.

        :return: Returns the most current message.
        '''
        self.new_message = False
        return self.last_message
    
    def my_loop(self):
        '''
        Function to loop the mqtt-client. Must be called regurarely.

        :return: Returns nothing.
        '''
        self.client.loop()

