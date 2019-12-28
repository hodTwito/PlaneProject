import socket


def IsAlive():
	ServerAddrIsAlive = '0.0.0.0'
	ServerPortIsAlive = 8000
	ServerIsAlive = (ServerAddrIsAlive, ServerPortIsAlive)

	IsAliveSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	IsAliveSock.bind(ServerIsAlive)

	print "Listening to " + ServerAddrIsAlive + " : " + str(ServerPortIsAlive)
	
	while True:
		IsAliveSock.settimeout(2)
		try:
			(comand, OperatorAddr) = IsAliveSock.recvfrom(1024)
			OperatorAddr = (OperatorAddr[0], 5000)
			if comand == "IamAlive":
				IsAliveSock.sendto("IamAlive", OperatorAddr)
		except socket.timeout:
			print "Connection Lost"
			#ConnectionLost()     -Function does NOT exist
					




