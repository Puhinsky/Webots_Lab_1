from controller import Robot
from math import pi

class RobotController(object):

    def __init__(self, robotParameters):
        self.robot = Robot()
        self.robotParameters = robotParameters
        self.leftMotor = self.motorInit('left wheel motor')
        self.rightMotor = self.motorInit('right wheel motor')
        self.timeStep = int(self.robot.getBasicTimeStep())

    def motorInit(self, motorName):
        motor = self.robot.getDevice(motorName)
        motor.setPosition(float('inf'))
        return motor

    def wait(self, delay):
        startTime = self.robot.getTime()
        while self.robot.step(self.timeStep) != -1:
            if self.robot.getTime() - startTime >= delay:
                break

    def stop(self):
        self.leftMotor.setVelocity(0)
        self.rightMotor.setVelocity(0)

    def getAbsoluteSpeed(self, percent):
        return self.robotParameters.maxWheelSpeed * percent / 100

    def getRadialSpeed(self, linearSpeed):
        return linearSpeed / self.robotParameters.wheelRadius

    def getLinearSpeed(self, radialSpeed):
        return radialSpeed * self.robotParameters.wheelRadius

    def getArcDifferenceRatio(self, radius):
        return (radius - self.robotParameters.robotWidth / 2) / (radius + self.robotParameters.robotWidth / 2)

    def getArcMoveTime(self, radius, angle, radialSpeed):
        return abs((2 * pi * radius * angle / 360) / self.getLinearSpeed(radialSpeed))
    
    def fixTime(self, time):
       return time * 1.1

    def moveOnLine(self, distance, relativeSpeed):
        radialSpeed = self.getAbsoluteSpeed(relativeSpeed)
        self.leftMotor.setVelocity(radialSpeed)
        self.rightMotor.setVelocity(radialSpeed)
        self.wait(distance/self.getLinearSpeed(radialSpeed))
        self.stop()

    def moveOnArc(self, radius, angle, relativeSpeed):
        externalWheelSpeed = self.getAbsoluteSpeed(relativeSpeed)
        internalWheelSpeed = externalWheelSpeed * self.getArcDifferenceRatio(radius)
        time = self.getArcMoveTime(radius + self.robotParameters.robotWidth / 2, angle, externalWheelSpeed)
        self.leftMotor.setVelocity(internalWheelSpeed)
        self.rightMotor.setVelocity(externalWheelSpeed)
        self.wait(self.fixTime(time))
        self.stop()

    def turnOnPlace(self, angle, relativeSpeed):
        speed = self.getAbsoluteSpeed(relativeSpeed)
        time = self.getArcMoveTime(self.robotParameters.robotWidth / 2, angle, speed)
        self.leftMotor.setVelocity(-speed)
        self.rightMotor.setVelocity(speed)
        self.wait(self.fixTime(time))
        self.stop()

