class TrajectoryPlayer(object):

    def __init__(self, trajectories):
        self.trajectories = trajectories

    def start(self, relativeSpeed):
        for trajectory in self.trajectories:
            trajectory.execute(relativeSpeed)