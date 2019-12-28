import socket
import Vars as GlobalVars


class Listener:
	def __init__(self, globalVars):
		self.globalVars = globalVars
	
	def Listen(self):	
		print "Listener In Function"
		ListenerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		ListenerAddr = ('0.0.0.0', 6001)
		ListenerSocket.bind(ListenerAddr)
		while True:	
			try:
				echo = ListenerSocket.recvfrom(1024)
				val = int(echo[0].split(" ")[1])
				print echo[0] + " Comfirmed \n\r"
				if echo[0].split(" ")[0] == "Sync":
					self.Sync(echo[0].split(" ")[1])
				elif echo[0] == "Engine75 0":
					self.globalVars.CurrentEngineSpeed = 75
					print "Current Engine speed is 75 % \n\r"
				elif echo[0] == "EngineStop 0":
					self.globalVars.CurrentEngineSpeed = 0
					print "Engine is stopped completely"
				elif echo[0] == "MaxSpeed 0":
					self.globalVars.CurrentEngineSpeed = 100
					print "Engine is running on full speed \n\r"
				elif echo[0].split(" ")[0] == "DecreaseEngineSpeed":
					self.globalVars.CurrentEngineSpeed = self.globalVars.CurrentEngineSpeed - 5
					print "Engine slowed down by 5%. current speed is " + str(self.globalVars.CurrentEngineSpeed) + "% \n\r"
				elif echo[0].split(" ")[0] == "IncreaseEngineSpeed":	
					self.globalVars.CurrentEngineSpeed = self.globalVars.CurrentEngineSpeed + 5
					print "Engine sped up by 5%. current speed is " + str(self.globalVars.CurrentEngineSpeed) + "% \n\r"
				elif echo[0].split(" ")[0] == "Rudder":
					if val == 0:
						self.globalVars.Rudder = (0, "0")
						print "Rudder is LEVELED  \n\r"
					elif val>0:
						self.globalVars.Rudder = (val, "L")
						print "Rudder is Set " + str(val) + " percent to the LEFT \n\r"
					elif val < 0:
						self.globalVars.Rudder = (abs(val), "R")
						print "Rudder is Set " + str(abs(val)) + " percent to the RIGHT \n\r"
				elif echo[0].split(" ")[0] == "Elevator":
					if val == 0:
						self.globalVars.Elevators = (0, "0")
						print "Elevators are LEVELED  \n\r"
					elif val>0:
						self.globalVars.Elevators = (val, "U")
						print "Elevators are Set " + str(val) + " percent UP \n\r"
					elif val < 0:
						self.globalVars.Elevators = (abs(val), "D")
						print "Elevators are Set " + str(abs(val)) + " percent DOWN \n\r"
				elif echo[0].split(" ")[0] == "Ailerons":
					if val == 0:
						self.globalVars.Ailerons = (0, "0")
						print "Ailerons are LEVELED  \n\r"
					elif val>0:
						self.globalVars.Ailerons = (val, "R")
						print "Ailerons are Set " + str(val) + " percent to the RIGHT \n\r"
					elif val < 0:
						self.globalVars.Ailerons = (abs(val), "L")
						print "Ailerons are Set " + str(abs(val)) + " percent to the LEFT \n\r"
			except socket.error:
				print "Socket Error Acured"   #if socket have diconnected (mainly on plany side) !@!@!@!@!@!@!@!@!
		ListenerSocket.close()
		print "Listener is closed"

	def Sync(self, SyncData):     #FIX THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		self.globalVars.Rudder = (SyncData[0], SyncData[1])
		self.globalVars.Elevators = (SyncData[2], SyncData[3])
		self.globalVars.Ailerons = (SyncData[4], SyncData[5])
		self.globalVars.CurrentEngineSpeed = int(SyncData[6] + SyncData[7])
		print "SyncIsComplete"