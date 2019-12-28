import socket, time
import ControlFunctions as CF
import PlaneVars
import threading

ServerAddr = '0.0.0.0'
ServerPort = 9001
Server = (ServerAddr, ServerPort)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(Server)
print "Listening to " + ServerAddr + " : " + str(ServerPort)

FirstTimeSync=True

def ServerSet(sock):
	global Server, FirstTimeSync
	while True:
		try:
			(comand, OperatorAddr) = sock.recvfrom(1024)
			#print comand
			OperatorAddr = (OperatorAddr[0], 6001)
			RealComand = comand.split(" ")[0]
			Value = int(comand.split(" ")[1])
			try:
				if RealComand != "Sync":
					#print "no problem"   #LOL
					sock.sendto(comand, OperatorAddr)
					if RealComand=="Engine75":
						CF.Engine75()
					elif RealComand=="EngineStop":
						CF.EngineStop()
					elif RealComand=="IncreaseEngineSpeed":
						CF.EngineSpeedUP()
					elif RealComand=="DecreaseEngineSpeed":
						CF.EngineSpeedDOWN()
					elif RealComand=="MaxSpeed":
						CF.EngineMaxSpeed()
					elif RealComand=="Ailerons":
						CF.Ailerons(Value)
					elif RealComand=="Rudder":
						CF.Rudder(Value)
					elif RealComand=="Elevator":
						CF.Elevator(Value)

				else:
					print "Sending Sync Data"
					sock.sendto("Sync" + " " + PlaneVars.GetAll(), OperatorAddr)
			except:
				print "Error 1"
		except:
			sock.close()
			newSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			newSock.bind(Server)
			print "Listening to " + ServerAddr + " : " + str(ServerPort)
			ServerSet(newSock)

			
ServerSet(sock)