from LineTrajectoryProcessor import LineTrajectoryProcessor
from TurnTrajectoryProcessor import TurnTrajectoryProcessor

class NGonTrajectory(object):

    def __init__(self, robotController, sideLenght, sidesCount):
        self.robotController = robotController
        self.sidesCount = sidesCount
        self.trajectories = []

        externalAngle = 360.0 / self.sidesCount

        for i in range(self.sidesCount):
            self.trajectories.append(LineTrajectoryProcessor(self.robotController, sideLenght))
            self.trajectories.append(TurnTrajectoryProcessor(self.robotController, externalAngle))

    def Start(self, relativeSpeed):
        for trajectory in self.trajectories:
            trajectory.execute(relativeSpeed)
