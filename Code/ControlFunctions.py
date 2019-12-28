import PlaneVars as GlobalVars

'''PLANE functions - Engine'''

def EngineSpeedUP():
	# Increase Engine Speed By 5%
	GlobalVars.CurrentEngineSpeed+=5
	print "Current Engine Speed is "  + str(GlobalVars.CurrentEngineSpeed)

def EngineSpeedDOWN():
	# Decrease Engine Speed By 5%
	GlobalVars.CurrentEngineSpeed-=5
	print "Current Engine Speed is " + str(GlobalVars.CurrentEngineSpeed)

def EngineMaxSpeed():
	#Set Engine Speed at 100 %
	GlobalVars.CurrentEngineSpeed=100
	print "Current Engine Speed is " + str(GlobalVars.CurrentEngineSpeed)

def EngineStop():
	# Set Engine Speed to 0
	GlobalVars.CurrentEngineSpeed=0
	print "Engine is stopped"
	
def Engine75():
	# Set Engine Speed to 75 %
	GlobalVars.CurrentEngineSpeed = 75
	print "Current Engine Speed is Set to " + str(GlobalVars.CurrentEngineSpeed)
		
'''PLANE functions - Control Surfaces'''

def Rudder(percent):
	# Set Rudder to percent
	if percent==0:
		GlobalVars.Rudder=(0,"0")
		print "Rudder is leveled"
	elif percent>0:
		GlobalVars.Rudder = (percent, "L")
		print "Rudder is Set " + str(percent) + " percent to the LEFT"
	elif percent < 0:
		GlobalVars.Rudder = (abs(percent), "R")
		print "Rudder is Set " + str(abs(percent)) + " percent to the RIGHT"
		

def Elevator(percent):
	# Set Elevator to percent
	if percent==0:
		GlobalVars.Elevators=(0,"0")
		print "Elevator is leveled"
	elif percent>0:
		GlobalVars.Elevators = (percent, "U")
		print "Elevator is Set " + str(percent) + " percent UP"
	elif percent < 0:
		GlobalVars.Elevators = (abs(percent), "D")
		print "Elevator is Set " + str(abs(percent)) + " percent DOWN"
		

def Ailerons(percent):
	# Set Ailerons to percent
	if percent==0:
		GlobalVars.Ailerons=(0,"0")
		print "Ailerons are leveled"
	elif percent>0:
		GlobalVars.Ailerons = (percent, "R")
		print "Ailerons are Set " + str(percent) + " percent to the RIGHT"
	elif percent < 0:
		GlobalVars.Ailerons = (abs(percent), "L")
		print "Ailerons are Set " + str(abs(percent)) + " percent to the LEFT"