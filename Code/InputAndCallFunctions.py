import pygame, sys, os
from time import sleep
import ModelControlFunctions as MCF
from pygame.locals import *


class InputAndCallFunctions:
	def __init__(self, mcf):
		'''controller state globals'''
		self.Buttonstate=[0,0,0,0,0,0,0,0,0,0]  #holds button state (Pressed/Unpressed)
		self.rudder=0
		self.elevator=0
		self.ailerons=0
		self.shift=0
		self.JoystickLock = True
		self.mcf = mcf
		
		self.joystickInit()
		self.MainLoop()
	
	def joystickInit(self):
		# setup the pygame window
		pygame.init()
		window = pygame.display.set_mode((200, 200), 0, 32) 	#for keyboard events

		# how many joysticks are connected to computer?
		joystick_count = pygame.joystick.get_count()
		print "\n\rThere is " + str(joystick_count) + " joystick/s"

		if joystick_count == 0:
			# if no joysticks, quit program safely
			print ("\n\rError, I did not find any joysticks")
			pygame.quit()
			sys.exit()
		else:
			# initialise joystick
			self.joystick = pygame.joystick.Joystick(0)
			self.joystick.init()
			print self.joystick.get_name() + " \n\r"
		self.axes = self.joystick.get_numaxes()
		self.buttons = self.joystick.get_numbuttons()
		self.hats = self.joystick.get_numhats()

		print "There is " + str(self.axes) + " axes"
		print "There is " + str(self.buttons) + " button/s"
		print "There is " + str(self.hats) + " hat/s \n\r"
		print "\n\rJoystickLock is ON, Press \"select\" to Active Controller input \r\n"



	def getAxis(self, number):		
		# when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
		# so this is used not "if joystick value not zero"
		if self.joystick.get_axis(number) < -0.1 or self.joystick.get_axis(number) > 0.1:
			# value between 1.0 and -1.0
			#print "Axis value is %s" %(joystick.get_axis(number))				Axis Value Print DISABLED
			#print "Axis ID is %s" %(number)									Axis ID Print DISABLED 
			'''foreach joystick, check its state'''
			if number==2:
				self.mcf.Rudder(self.mcf.InputToPercent(self.joystick.get_axis(number)))
				rudder = 1
			elif number==3:
				self.mcf.Elevator(self.mcf.InputToPercent(self.joystick.get_axis(number)))
				elevator=1
			elif number==0:
				self.mcf.Ailerons(self.mcf.InputToPercent(self.joystick.get_axis(number)))
				ailerons=1 
			
		#if rudder/elevator/aileron axis = 0 (is not pressed), but was in pressed position before - Level to Surface
		else:
			if number==2 and self.rudder==1: 
				self.mcf.Rudder(0)
				self.rudder = 0
			elif number==3 and self.elevator==1: 
				self.mcf.Elevator(0)
				self.elevator = 0
			elif number==0 and self.ailerons==1: 
				self.mcf.Ailerons(0)
				self.ailerons = 0
			
	def getButton(self, number):
		# if button is pressed, and if it was not pressed before - execute the appropriate function
		if self.joystick.get_button(number) and self.Buttonstate[number] == 0:
			#print "Button ID is %s" %(number) 								#Button ID print DISABLED
			self.Buttonstate[number] = 1
			if number==3:
				self.mcf.Engine75()
			elif number==1 and self.shift==1:
				self.mcf.EngineStop()
			elif number==1 and not self.shift:
				print "press and hold L1"
			elif number==4 and self.shift==0:
				self.shift = 1
				print "shift on " + str(self.shift) + "\n\r"
			elif number == 6 and  not self.JoystickLock:
				self.JoystickLock = True
				print "JoystickLock is ON \n\r"
			elif number == 6 and self.JoystickLock:
				self.JoystickLock = False
				print "JoystickLock is OFF \n\r"
		# if button state is "isn't pressed" and it was pressed before - reset Buttonstate list to 0
		if not self.joystick.get_button(number) and self.Buttonstate[number] == 1:
			#print Buttonstate
			self.Buttonstate[number] = 0
		if number == 4 and (not self.joystick.get_button(number)):	 
			if self.shift == 1:
				self.shift = 0 
				print "shift off " + str(self.shift) + "\n\r"
			

	def getHat(self, number):
		if self.joystick.get_hat(number) != (0,0):
			# returns tuple with values either 1, 0 or -1
			#print "Hat value is %s, %s" %(joystick.get_hat(number)[0],joystick.get_hat(number)[1])
			#print "Hat ID is %s" %(number)																Hat Value print DISABLED
			if self.joystick.get_hat(number) == (0,1):
				self.mcf.EngineSpeedUP()
			elif self.joystick.get_hat(number) == (0,-1):
				self.mcf.EngineSpeedDOWN()
		
	def MainLoop(self):
		while True:
			for event in pygame.event.get():
				# loop through events, if F1 is pressed, quit program, if BACKSPACE is pressed, clean promt
				if event.type == pygame.KEYDOWN:
					print "Detected KeyDown"
					if event.key == K_F1:
						print "F1 pressed"
						self.mcf.CloseConnection() #Close Connection
						pygame.quit()
						sys.exit()
					elif event.key == K_BACKSPACE:
						os.system("cls")
			if self.axes != 0:
				if self.JoystickLock==False:
					for i in range(self.axes):
						self.getAxis(i)
			if self.buttons != 0:
				if self.JoystickLock==False:
				  for i in range(self.buttons):
					self.getButton(i)
				else:
					self.getButton(6)
			if self.hats != 0:
				if self.JoystickLock==False:
					for i in range(self.hats):
						self.getHat(i)
			sleep(0.1)