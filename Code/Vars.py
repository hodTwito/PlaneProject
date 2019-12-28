#Operator Side Global Variables

class Vars:
	def __init__(self):
		self.currentEngineSpeed = 0  #Percent
		self.rudder = (0,"0")  #(percent, "0/R/L")
		self.elevators = (0,"0")  #(percent, "0/U/D")
		self.ailerons = (0,"0")  #(percent, "0/R/L")
		self.killAllThreads = False
		self.listOfCommands = [] #Values Are Tuples (Command, Time)
		#self.activeThreads = []