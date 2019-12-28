import ModelControlFunctions as MCF
import InputAndCallFunctions as IACF


mcf = MCF.ModelControlFunctions()

#mcf.OpenConnection()	#open socket connection and Activate IsAlive Loop

iacf = IACF.InputAndCallFunctions(mcf)
#IACF.MainLoop()		#loop and check for events
