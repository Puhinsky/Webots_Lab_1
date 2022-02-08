class TurnTrajectoryProcessor(object):
    
    def __init__(self, robotController, angle):
        self.robotController = robotController
        self.angle = angle

    def execute(self, relativeSpeed):
        self.robotController.turnOnPlace(self.angle, relativeSpeed)