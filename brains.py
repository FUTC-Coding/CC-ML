#
# BRAINS
#
# Add in this file your brain class. Look at the two example brains for inspiration.
#
from lib.car import Brain
from lib.sensors import Sensor, GoalSensor


class InteractiveBrain(Brain):
    """Brain that allows to control a car with the arrow keys."""
    def setup(self):
        def up(event):
            self.car.accelerate(1)

        def down(event):
            self.car.accelerate(-1)

        def right(event):
            self.car.turn(15)

        def left(event):
            self.car.turn(-15) 

        self.track.canvas.focus_force()  # listen

        self.track.canvas.bind('<Up>', up)
        self.track.canvas.bind('<Down>', down)
        self.track.canvas.bind('<Right>', right)
        self.track.canvas.bind('<Left>', left)

    def update(self):
        pass


class InteractiveBrainWithSensors(InteractiveBrain):
    """Brain that allows to control a car with the arrow keys and that installs sensors on the car."""
    def setup(self):
        super(InteractiveBrainWithSensors, self).setup()
        
        self.front_left_sensor = Sensor(self.car, angle=-2, x=-6, y=15)
        self.front_center_sensor = Sensor(self.car, angle=0, x=0, y=15)
        self.front_right_sensor = Sensor(self.car, angle=2, x=6, y=15)
        self.goal_sensor = GoalSensor(self.car)       

    def update(self):
        print(self.car.sensors)
        print(f"[sensor] distance: {self.front_center_sensor.distance}, is_goal: {self.front_center_sensor.is_obstacle_goal}")
        print(f"[car] speed: {self.car.speed}, direction: {self.car.direction}")
