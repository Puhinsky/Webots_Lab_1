class LineTrajectoryProcessor(object):

    def __init__(self, robotController, distance):
        self.robotController = robotController
        self.distance = distance

    def execute(self, relativeSpeed):
        self.robotController.moveOnLine(self.distance, relativeSpeed)