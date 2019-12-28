import os
import time

os.system("sudo killall pigpiod")
time.sleep(2)
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1)
import pigpio #importing GPIO library

class Engine:
    def __init__(self):
        #os.system("sudo killall pigpiod")
        #time.sleep(1)
        #os.system("sudo pigpiod")
        #time.sleep(1)
        #import pigpio
        
        self.enginePin = 4
        
        self.maxSpeed = 2369
        self.minSpeed = 1139
        
        self.pi = pigpio.pi()
        self.pi.set_servo_pulsewidth(self.enginePin, 0)
        self.currentSpeed=0
        
        self.arm()
        
    def precentToPulse(self, precent):
        if precent <= 0.082 or precent > 100:
            return 0
        pulse = self.minSpeed + (precent * (self.maxSpeed - self.minSpeed)) / 100
        print(pulse)
        return pulse
    
    def rotate(self, precent):
        try:
            newSpeed = self.precentToPulse(precent)
            self.pi.set_servo_pulsewidth(self.enginePin, newSpeed)
            self.currentSpeed = newSpeed
        except Exception as e:
            self.stop(e)
    
    def arm(self):
        self.pi.set_servo_pulsewidth(self.enginePin, 0)
        time.sleep(1)
        #self.pi.set_servo_pulsewidth(self.enginePin, self.maxSpeed)
        #time.sleep(1)
        self.pi.set_servo_pulsewidth(self.enginePin, 1050)
        time.sleep(2)
                 
    def drive(self, speed):
        self.pi.set_servo_pulsewidth(self.enginePin, speed)

    def stop(self, error=""):
        self.pi.set_servo_pulsewidth(self.enginePin, 0)
        self.pi.stop()
        if error != "":
            print(error)
        print("engine stoped!")