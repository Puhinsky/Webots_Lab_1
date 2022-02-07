"""Trajectory_Follower_Controller controller."""

from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    pass
