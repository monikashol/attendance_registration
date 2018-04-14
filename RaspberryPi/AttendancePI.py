from stmpy import Machine, Driver 
import paho.mqtt.client as mqtt
import json

class RasPi: 

	#Here we save the beacon adresses (hard coded)
	adresses = []

	#RasPi listens for and handles bluetooth signals 
	def listen(self):
		print("Listens...")
		self.startTimer()
	
	def setup(self):
		print("Setting up...")
		self.startTimer()

	def startTimer(self): 
		#print("Timer started")
		time = 1000*5
		self.stm.start_timer('t', 1000)
		


	def send(self): 
		print("Sending message...")
		self.startTimer()


#Making the RasPi object
raspi = RasPi()


#TRANSITIONS

#To the state  where RasPi listens for signals from Beacon
t0 = {	
	'source': 'initial',
	'target': 'setup'
	 }

t1 = {	
	'trigger': 't',
	'source': 'setup', 
	'target': 'receiver'
	}

t2 = {	
	'trigger': 't',
	'source': 'receiver',
	'target': 'transmitter'
	}

t3 = {	
	'trigger': 't',
	'source': 'transmitter',
	'target': 'receiver'
	}




#STATES

setup = {
	'name': 'setup', 
	'entry': 'setup'
}

#The receiver state where RasPi listens for signals
receiver = { 
	'name': 'receiver',
	'entry': 'listen'
	}

#The transmitter state where RasPi transmit message to the mqtt-broker
transmitter = {	
	'name': 'transmitter', 
	'entry': 'send'
	} 


#STATE MACHINE
machine = Machine(name='raspi', transitions=[t0, t1, t2, t3], obj=raspi, states=[setup, receiver, transmitter])
raspi.stm = machine

#Setting up and starting the driver
driver = Driver()
driver.add_machine(machine)
driver.start()

