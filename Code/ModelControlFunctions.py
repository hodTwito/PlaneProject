import socket 
import OperatorSideComs as OSC
import Vars as GlobalVars
#import InputAndCallFunctions as IACF

class ModelControlFunctions:
	def __init__(self):
		self.globalVars = GlobalVars.Vars()
		self.osc = OSC.OperatorSideComs(self.globalVars)
		self.OpenConnection()
		
		#iacf = IACF.InputAndCallFunctions(self)
		
	'''opening UDP connection with model'''
	def OpenConnection(self):
		self.osc.OpenConnection()

	'''closing connection with model'''
	def CloseConnection(self):
		self.osc.CloseConnection()

	'''model functions - Engine'''
	def EngineSpeedUP(self):
		#global GlobalVars.CurrentEngineSpeed
		if self.globalVars.CurrentEngineSpeed<96:
			self.osc.SendCommand("IncreaseEngineSpeed", self.globalVars.CurrentEngineSpeed + 5) #send comand to increase engine speed by 5%
			#GlobalVars.CurrentEngineSpeed = GlobalVars.CurrentEngineSpeed + 5
		elif self.globalVars.CurrentEngineSpeed<100:
			self.osc.SendCommand("MaxSpeed") #Send comand to max engine speed"
			#GlobalVars.CurrentEngineSpeed = 100
		else:
			print "Engine is already running on full speed \n\r"
	def EngineSpeedDOWN(self):
		#global GlobalVars.CurrentEngineSpeed
		if self.globalVars.CurrentEngineSpeed>4:
			self.osc.SendCommand("DecreaseEngineSpeed", self.globalVars.CurrentEngineSpeed - 5) #send comand to decrease engine speed by 5%
			#GlobalVars.CurrentEngineSpeed = GlobalVars.CurrentEngineSpeed - 5
		elif self.globalVars.CurrentEngineSpeed>0:
			self.EngineStop()
			print "Engine is stopped"
		else:
			print "Engine is already stopped"
	def EngineStop(self):
		#global GlobalVars.CurrentEngineSpeed
		self.osc.SendCommand("EngineStop") #send comand to stop engine completely"
		#GlobalVars.CurrentEngineSpeed = 0
	def Engine75(self):
		#global GlobalVars.CurrentEngineSpeed
		if self.globalVars.CurrentEngineSpeed!=75:
			self.osc.SendCommand("Engine75") #send comand to set engine speed on 75%"
			#GlobalVars.CurrentEngineSpeed = 75
		else:
			print "Engine is already on 75% \n\r"
			
	'''model functions - Control Surfaces'''
	def Rudder(self, percent):
		self.osc.SendCommand("Rudder", percent) #send comand to set Rudder to a specific position
	def Elevator(self, percent):
		self.osc.SendCommand("Elevator", percent) #send comand to set Elevator to a specific position
	def Ailerons(self, percent):
		self.osc.SendCommand("Ailerons", percent) #send comand to set Elevator to a specific position
	
	'''Converter'''
	def InputToPercent(self, a):
		return (int(round(a,2)*100)/5)*5 #EXAMPLE: gets 0.66946384354 and returns 65