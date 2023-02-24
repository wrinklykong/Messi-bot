#!/usr/bin/python3
import serial
import time
import brickpi3 

BP = brickpi3.BrickPi3() 
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.NONE)
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_GYRO_ABS)
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

class RobotLib():
    # for finding its way back
    def __init__(self, port, baudrate=9600, timeout=1):
        
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        
        print("*** Press the GREEN button to start the robot ***")
        
        time.sleep(2)
        
        while True:
            print("--- Sending out handshaking signal ---")
            ack = self.cmdSend(1)
            if not ack:
                print("*** Try again ***")
                print("*** Press the GREEN button to start the robot ***")
            else:
                print("!!! Connected to the robot !!!")
                
                # clear the serial receive buffer
                self.ser.readall()
                break
            
    def cmdSend(self, cmd, para=0):
        
        msg = str(cmd) + str(para) + "\n"
        
        s1 = time.time()
        self.ser.write(msg.encode())
        e1 = time.time()
        
        # originally received msg will end with '\r\n'
        ack_origin = self.ser.readline()
        
        # we can skip the last two bytes
        ack = ack_origin[:-2].decode("utf-8")
        return ack
    
    def turnLeft(self, power=15):
        # 2 is the left turn cmd
        ack = self.cmdSend(2, power)
    
    def turnRight(self, power=15):
        # 3 is the right turn cmd
        ack = self.cmdSend(3, power)
        
    def moveForward(self, power=10):
        # 4 is the move forward cmd
        ack = self.cmdSend(4, power)
        
    def moveBack(self, power=10):
        # 5 is the move backward cmd
        ack = self.cmdSend(5, power)
        
    def getDistance(self, sensorPort=3):
        # 6 is the distance cmd
        ack = self.cmdSend(6, sensorPort)
        
        return int(ack[1:])
    
    def stopMotor(self):
        # 7 is the stop cmd
        ack = self.cmdSend(7)
        
    def brakeMotor(self):
        # 8 is the brake cmd
        ack = self.cmdSend(8)
        
    def skrrt(self):
        # 6 is the distance cmd
        ack = self.cmdSend(9)
        
    def kick(self):
        # 6 is the distance cmd
        ack = self.cmdSend(6)
        
    def colorSensor(self):
            try:
              value = BP.get_sensor(BP.PORT_3)
            #tValue = BP.get_sensor(BP.PORT_4)
              print(color[value])                # print the color
            #print(speed[value])
            #BP.set_motor_power(BP.PORT_B, speed[value])
            except brickpi3.SensorError as error:
              print(error)
        
            return value
        
    def gyroSensor(self):
        value = BP.get_sensor(BP.PORT_1)
        return value
    
    def turnLeftCertainDegree(self, degree):
        initAngle = self.gyroSensor()
        newAngle = initAngle
        self.turnLeft()
        while ( initAngle-newAngle < degree-5 ):
            self.turnLeft()
            newAngle=self.gyroSensor()
            print(newAngle)
        self.turnRight()
        self.stopMotor()
      
    def turnRightCertainDegree(self, degree):
        initAngle = self.gyroSensor()
        newAngle = initAngle
        self.turnRight()
        while ( newAngle-initAngle < degree-5 ):
            self.turnRight()
            newAngle=self.gyroSensor()
            print(newAngle)
        self.turnLeft()
        self.stopMotor()
        
    def setAngle(self, curr, degree):
        current = curr%360;
        difference = degree-current;
        if difference > 0:
            if difference > 180:
                difference=0-(difference-180);
            # turn left
            self.turnLeftCertainDegree(abs(difference));
        else:
            if difference < 180:
                difference=abs(difference+180);
            # turn right
            self.turnRightCertainDegree(abs(difference));
        return curr+difference;
    
    def goHome():
        current = 0;
