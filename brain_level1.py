#
# BRAINS
#
# Add in this file your brain class. Look at the two example brains for inspiration.
#
from lib.car import Brain
from lib.sensors import Sensor, GoalSensor
import random
import os
import os.path

class RandomBrain(Brain):

    def setup(self):
        if os.path.isfile("best"):
            with open("best", "r") as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                #print(content)

        #self.car.accelerate(4)
        #self.front_left_sensor = Sensor(self.car, angle=-2, x=-6, y=15)
        self.front_center_sensor = Sensor(self.car, angle=0, x=0,y=15)
        #self.front_right_sensor = Sensor(self.car, angle=2, x=6, y=15)
        self.right_sensor = Sensor(self.car, angle=70,x=6,y=15)
        self.left_sensor = Sensor(self.car, angle=-70, x=-6, y=15)
        self.goal_sensor = GoalSensor(self.car)

        if not os.path.isfile("best"):
            self.best = self.goal_sensor.distance + 1
            self.bestTurn = 0
            self.bestAccel = 0
            self.bestDistanceSides = 0
            self.bestDistanceFront = 0
            self.generation = 1
            self.currentGeneration = 1

            self.turn = random.randrange(90)
            self.accel = random.randrange(10)
            self.distance_sides = random.randrange(100)
            self.distance_front = random.randrange(100)
        else:
            self.best = (float(content[0]))
            print(self.best)
            self.bestTurn = float(content[1])
            self.bestAccel = float(content[2])
            self.bestDistanceFront = float(content[3])
            self.bestDistanceSides = float(content[4])
            self.generation = int(content[5])
            self.currentGeneration = self.generation + 1

            # use 20% surrounding the best previous turn value to calc new random range
            self.turn = random.uniform(self.bestTurn - self.bestTurn / 10, self.bestTurn + self.bestTurn / 10)
            self.accel = random.uniform(self.bestAccel - self.bestAccel / 10, self.bestAccel + self.bestAccel / 10)
            self.distance_front = random.uniform(self.bestDistanceFront - self.bestDistanceFront / 10, self.bestDistanceFront + self.bestDistanceFront / 10)
            self.distance_sides = random.uniform(self.bestDistanceSides - self.bestDistanceSides / 10, self.bestDistanceSides + self.bestDistanceSides / 10)



    def update(self):
        #print("turn speed: " + str(self.turn))
        #print("accel speed: " + str(self.accel))
        #print("distance sides: " + str(self.distance_sides))
        #print("distance front: " + str(self.distance_front))
        # print("left:" + str(self.left_sensor.distance))
        # print("right:" + str(self.right_sensor.distance))
        # print("center:" + str(self.front_center_sensor.distance))
        # print("speed" + str(self.car.speed))
        #print(self.right_sensor.distance)
        #if self.goal_sensor.distance < 400:
            #self.car.accelerate(10)

        if self.front_center_sensor.is_obstacle_goal:
            pass
        elif self.left_sensor.distance < self.distance_sides or self.right_sensor.distance < self.distance_sides or self.front_center_sensor.distance < self.distance_front:
            if self.left_sensor.distance < self.right_sensor.distance:
                    self.car.turn(self.turn)
            elif self.left_sensor.distance > self.right_sensor.distance:
                    self.car.turn(-self.turn)

        if self.car.speed == 0:
            self.car.accelerate(self.accel)

        if self.goal_sensor.distance < int(self.best) & self.currentGeneration == self.generation:
            if os.path.isfile("best"):
                os.remove("best")

            print("written")

            self.best = self.goal_sensor.distance
            self.bestTurn = self.turn
            self.bestAccel = self.accel
            self.bestDistanceSides = self.distance_sides
            self.bestDistanceFront = self.distance_front
            file = open("best", "w")
            file.write(str(self.best) + "\n")
            file.write(str(self.bestTurn) + "\n")
            file.write(str(self.bestAccel) + "\n")
            file.write(str(self.bestDistanceFront) + "\n")
            file.write(str(self.bestDistanceSides) + "\n")
            file.write(str(self.generation))
            file.close()


class scriptedBrain(Brain):
    def setup(self):
        self.car.accelerate(4)
        self.ticks = 0
        pass

    def update(self):
        self.ticks += 1
        print(self.ticks)
        if self.ticks == 100:
            self.car.turn(90)
        elif self.ticks == 250:
            self.car.turn(90)
        elif self.ticks == 350:
            self.car.turn(90)
        pass

class SensorBrain(Brain):
    def setup(self):
        #self.car.accelerate(4)
        #self.front_left_sensor = Sensor(self.car, angle=-2, x=-6, y=15)
        self.front_center_sensor = Sensor(self.car, angle=0, x=0,y=15)
        #self.front_right_sensor = Sensor(self.car, angle=2, x=6, y=15)
        self.right_sensor = Sensor(self.car, angle=70,x=6,y=15)
        self.left_sensor = Sensor(self.car, angle=-70, x=-6, y=15)
        #self.goal_sensor = GoalSensor(self.car)

    def update(self):
        # print("left:" + str(self.left_sensor.distance))
        # print("right:" + str(self.right_sensor.distance))
        # print("center:" + str(self.front_center_sensor.distance))
        # print("speed" + str(self.car.speed))
        #print(self.right_sensor.distance)
        #if self.goal_sensor.distance < 400:
            #self.car.accelerate(10)

        if self.front_center_sensor.is_obstacle_goal:
            pass
        elif self.left_sensor.distance < 25 or self.right_sensor.distance < 25 or self.front_center_sensor.distance < 50:
            if self.left_sensor.distance < self.right_sensor.distance:
                    self.car.turn(6)
            elif self.left_sensor.distance > self.right_sensor.distance:
                    self.car.turn(-6)

        if self.car.speed == 0:
            self.car.accelerate(4)

