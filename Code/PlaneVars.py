#Plane Side Global Variables

CurrentEngineSpeed = 0  #Percent

Rudder = (0,"0")  #(percent, "R/L")
Elevators = (0,"0")  #(percent, "U/D")
Ailerons = (0,"0")  #(percent, "R/L")

def GetAll():		#will return Control Surfaces Values and position
	global Rudder, Elevators, Ailerons, CurrentEngineSpeed
	if CurrentEngineSpeed>5:
		return str(Rudder[0]) + Rudder[1] + str(Elevators[0]) + Elevators[1] + str(Ailerons[0]) + Ailerons[1] + str(CurrentEngineSpeed)
	else:
		return str(Rudder[0]) + Rudder[1] + str(Elevators[0]) + Elevators[1] + str(Ailerons[0]) + Ailerons[1] + "0" + str(CurrentEngineSpeed)
		