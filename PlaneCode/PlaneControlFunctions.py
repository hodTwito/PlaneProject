import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Control Pins
rightElevatorPin = 3 
leftElevatorPin = 5
rudderPin = 7
rightAeileronPin = 11
leftAeileronPin = 13


class PlaneControlFunctions:

    def __init__():
        #set Control Pins to OUTPUT mode
        GPIO.setup(rightElevatorPin, GPIO.OUT)
        GPIO.setup(leftElevatorPin, GPIO.OUT)
        GPIO.setup(rudderPin, GPIO.OUT)
        GPIO.setup(rightAeileronPin, GPIO.OUT)
        GPIO.setup(leftAeileronPin, GPIO.OUT)
        #Set Control Pins to PWM - 50 Hz
        self.rightElevator=GPIO.PWM(rightElevatorPin, 50)
        self.leftElevator=GPIO.PWM(leftElevatorPin, 50)
        self.rudder=GPIO.PWM(rudderPin, 50)
        self.rightAeileron=GPIO.PWM(rightAeileronPin, 50) 
        self.leftAeileron=GPIO.PWM(leftAeileronPin, 50) 
        #some stupid initialization
        self.rightElevator.start(0)
        self.leftElevator.start(0)
        self.rudder.start(0)
        self.rightAeileron.start(0)
        self.leftAeileron.start(0)
        #Set 0
        self.rightElevatorZero = 90
        self.leftElevatorZero = 90
        self.rudderZero = 90
        self.rightAeileronZero = 90
        self.leftAeleronZero = 90
        

        
    def Rudder(self, value):
        rudderMultiplier = 1
        SetToAngle(self.rudder, value,self.rudderZero, rudderMultiplier)
        
        
    def SetToAngle(pin, value, zero, Multiplier):
        angle=zero+(0.9*value*Multiplier)
        if angle<0:
            angle=0
        elif angle > 180:
            angle=180
        duty = angle/18 + 2.85
        pin.ChangeDutyCycle(duty)

   
