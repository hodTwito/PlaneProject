import socket, threading
import Vars as GlobalVars
from Listener import Listener
import time

class OperatorSideComs:

	def __init__(self, globalVars):
		self.ServerAddr = '127.0.0.1'   #Plane Address
		self.ServerPort = 9001 		    #Plane Port
		self.Server = (self.ServerAddr, self.ServerPort)
		self.sock = 0
		#self.FirstConnection = True
		self.SenderCounter = 1
		self.globalVars = globalVars
		self.listener = Listener(self.globalVars)
	
	def OpenConnection(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print "Connection OPENED \n\r"
		t = threading.Thread(target=self.listener.Listen, args=())
		t.start()
		print "Listener OK"
		time.sleep(0.5)
		self.SendCommand("Sync")
		print "Sync SENT"
		#threading.Thread(target=IsAliveSender, args=()).start()
		#threading.Thread(target=IsAliveReciever, args=()).start()
		print "IsAliveLoopSet"
		
	def CloseConnection(self):
		self.sock.close()
		#GlobalVars.KillAllThreads = True
		print "Connection CLOSED \n\r"

	def SendCommand(self, cmnd, val=0):
		#print "Sent Comand initiated"
		t = threading.Thread(target=self.Sender, args=(cmnd, self.sock, self.Server, val, ))
		t.start()
		
	def Sender(self, Command, SockHandle, Server, val):  #MUTEX!!!!!!!!!!!!!!!!!!!!!!!!
		SockHandle.sendto(Command + " " + str(val), Server)  # send Command + value to Server Addr
		#print "Sent " + Command
		self.globalVars.listOfCommands.append((self.SenderCounter, time.time(), Command, val))
		self.SenderCounter = self.SenderCounter + 1
		
			
	
	
	
	'''def IsAliveSender():
		while not GlobalVars.KillAllThreads:
			SendCommand("IamAlive")
			time.sleep(0.5)
			
	def IsAliveReciever():
		ThisPCAddr = '0.0.0.0'   #This PC ADDR
		ThisPCPort = 5000 		 #This PC port
		ThisPC = (ThisPCAddr, ThisPCPort)
		IsAliveReciever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		IsAliveReciever.bind(ThisPC)
		while True:
			IsAliveReciever.settimeout(2)
			try:
				msg = IsAliveReciever.recvfrom(1024)
				if msg=="IamAlive":
					pass
			except socket.timeout:
				# if 3 times there is no response - Connection Lost
				print "Connection Lost, Waiting for Response"
				IsAliveReciever.close()
				GlobalVars.KillAllThreads = True
				OpenConnection()
				break'''
					
