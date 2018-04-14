from stmpy import Driver, Machine 
import paho.mqtt.client as mqtt
import json

class Computer:
    
    broker = 'test.mosquitto.org'
    port = 1883

    #This is where the children and their corresponding bluetooth addresses are stored
    childAdress = {'address': 'child'}


    def mqttsubscribe(self):
        print("Trying to subscribe...")
        self.start_timer()



    #PC listens for and handles MQTT messages
    def mqttlisten(self): 
        print("Listens...")
        self.start_timer()


    def handleJSON(self): 
        print("Packet being handled...")
        self.start_timer()

    def start_timer(self):
        # start the timer
        self.stm.start_timer('t', 1000*2)


#Make computer object: 
computer = Computer()    


#TRANSITIONS

#The initial transition
t0 = {  
    'source': 'initial', 
    'target': 'setup'
    }

t1 = {  
    'trigger': 't',
    'source': 'setup', 
    'target': 'listen'
    }

t2 = {
    'trigger': 't',
    'source': 'listen', 
    'target': 'handle'
}

t3 = {
    'trigger': 't', 
    'source': 'handle', 
    'target': 'listen'
}



#STATES

setup = {
    'name': 'setup',
    'entry': 'mqttsubscribe'
}

listen = {
    'name': 'listen',
    'entry': 'mqttlisten' 
}

handle = {
    'name': 'handle', 
    'entry': 'handleJSON'
}


#STATE MACHINE
machine = Machine(name='computer', transitions=[t0, t1, t2, t3], obj=computer, states=[setup, listen, handle])
computer.stm = machine

#Setting up and starting the driver
driver = Driver()
driver.add_machine(machine)
driver.start()
