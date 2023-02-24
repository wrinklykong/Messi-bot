#!/usr/bin/python3
import time
from robotLib_jy import RobotLib
import random
import sys

port = "/dev/ttyUSB1"
baudrate = 9600

messiRobot = RobotLib(port, baudrate)
time.sleep(1)
random.seed(1)

start_time = time.time()
# For finding a way home,
# initial angle and x dist/y dist from origin
currentAngle = 0;
xDist = 0;
yDist = 0;
lastTurn = 0; #last turn was left, 0 is right

print(messiRobot.gyroSensor())

while True:
    color = messiRobot.colorSensor()
    #blue
#    if ( color == 2 ):
#        messiRobot.stopMotor()
#        time.sleep(2)
    #yellow, object, run the grab method and then its gonna go home
    if (color == 4):
        messiRobot.moveBack(10);
        messiRobot.stopMotor();
        # position object and then move forward
        time.sleep(1);
        messiRobot.moveBack(10);
        time.sleep(1);
        messiRobot.turnRightCertainDegree(90);
        time.sleep(0.5);
        messiRobot.moveForward(10);
        time.sleep(2);
        messiRobot.turnLeftCertainDegree(90);
        time.sleep(0.5);
        messiRobot.moveForward(10);
        time.sleep(3);
        messiRobot.turnLeftCertainDegree(90);
        time.sleep(0.5);
        messiRobot.moveForward(10);
        time.sleep(2);
        messiRobot.turnLeftCertainDegree(90);
        time.sleep(0.5);
        # go home
        while True:
            messiRobot.moveForward(8);
            color = messiRobot.colorSensor()
            if color == 6:
                # move back to safe area
                messiRobot.stopMotor();
                messiRobot.skrrt();
                time.sleep(2);
            #red, goal line
            elif color == 5:
                messiRobot.stopMotor();
                time.sleep(2);
                messiRobot.moveBack(10);
                time.sleep(0.25);
                #messiRobot.kick();
                messiRobot.moveForward(75);
                time.sleep(0.5);
                messiRobot.moveBack(50);
                time.sleep(2);
                messiRobot.stopMotor();
                exit();
                
        
    #white or red
    elif (color == 6 or color == 5): 
        #Go back into safe area
        messiRobot.moveBack(10)
        time.sleep(3)
        messiRobot.turnRightCertainDegree(random.randint(45,80))
        time.sleep(2)
    else:
        messiRobot.moveForward(10)
 
  
