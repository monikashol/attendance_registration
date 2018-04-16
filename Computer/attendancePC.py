from stmpy import Driver, Machine 
from graphviz import Source
import paho.mqtt.client as mqtt
import json


class Computer:

   
    #This is where the children and their corresponding bluetooth addresses are stored
    childAdress = {'address1': 'childA', 'address2': 'childB', 'address3': 'childC'}

    #Here is the children and their status stored. This is what will be shown on the monitor. 
    children = {'childA': 'status', 'childB': 'status', 'childC': 'status'}


    #PC listens for and handles MQTT messages
    def mqttlisten(self): 

        def on_message(client, userdata, msg): 
            message = json.loads(msg.payload.decode('utf-8'))
            print("Topic: " + msg.topic)
            print("Message: " + str(message))

        print("Listens...")
        broker = 'test.mosquitto.org'
        port = 1883
        client = mqtt.Client()
        client.on_message = on_message
        client.connect("test.mosquitto.org", 1883, 60)
        client.subscribe("mqtt_test/#")
        client.loop_forever()

        self.start_timer()


    def handleJSON(self): 
        print("Packet being handled...")
        self.start_timer()

    def start_timer(self):
        # start the timer
        time = 2*1000
        self.stm.start_timer('t', time)



#Make computer object: 
computer = Computer()    


#TRANSITIONS

#The initial transition
t0 = {  
    'source': 'initial', 
    'target': 'listen'
    }

t1 = {
    'trigger': 't',
    'source': 'listen', 
    'target': 'handle'
}

t2 = {
    'trigger': 't', 
    'source': 'handle', 
    'target': 'listen'
}



#STATES

listen = {
    'name': 'listen',
    'entry': 'mqttlisten' 
}

handle = {
    'name': 'handle', 
    'entry': 'handleJSON'
}



#STATE MACHINE
machine = Machine(name='computer', transitions=[t0, t1, t2], obj=computer, states=[listen, handle])
computer.stm = machine

#Setting up and starting the driver
driver = Driver()
driver.add_machine(machine)
driver.start()


