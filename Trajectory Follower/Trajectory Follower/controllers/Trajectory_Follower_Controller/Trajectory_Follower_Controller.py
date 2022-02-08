"""Trajectory_Follower_Controller controller."""

from RobotController import RobotController
from RobotParameters import RobotParameters

robotParameters = RobotParameters(6.28, 0.0205, 0.052)
robotController = RobotController(robotParameters)

#robotController.moveOnLine(0.25, 50)
robotController.moveOnArc(0.3, 270.0, 50)
#robotController.turnOnPlace(90, 50)

while robotController.robot.step(robotController.timeStep) != -1:
    pass