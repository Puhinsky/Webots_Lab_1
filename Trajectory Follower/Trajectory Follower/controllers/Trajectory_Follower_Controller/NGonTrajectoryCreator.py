from LineTrajectoryProcessor import LineTrajectoryProcessor
from TurnTrajectoryProcessor import TurnTrajectoryProcessor

class NGonTrajectoryCreator(object):

    def __init__ (self, robotController):
        self.robotController = robotController

    def createTrajectory(self, sideLenght, sidesCount):
        trajectories = []
        externalAngle = 360.0 / sidesCount
        for i in range(sidesCount):
            trajectories.append(LineTrajectoryProcessor(self.robotController, sideLenght))
            trajectories.append(TurnTrajectoryProcessor(self.robotController, externalAngle))
        return trajectories
