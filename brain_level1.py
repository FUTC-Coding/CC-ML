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
import time

class RandomBrain(Brain):
    def setup(self):
        #self.car.accelerate(4)
        #self.front_left_sensor = Sensor(self.car, angle=-2, x=-6, y=15)
        self.front_center_sensor = Sensor(self.car, angle=0, x=0,y=15)
        #self.front_right_sensor = Sensor(self.car, angle=2, x=6, y=15)
        self.right_sensor = Sensor(self.car, angle=70,x=6,y=15)
        self.left_sensor = Sensor(self.car, angle=-70, x=-6, y=15)
        self.goal_sensor = GoalSensor(self.car)
        self.time = time.time()

    def calcAttributes(self):
        if os.path.isfile("best"):
            with open("best", "r") as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                #print(content)

        if not os.path.isfile("best"):
            self.best = self.goal_sensor.distance
            self.bestTurn = 0
            self.bestAccel = 0
            self.bestDistanceSides = 0
            self.bestDistanceFront = 0
            self.generation = 0
            self.currentGeneration = 1
            self.bestTime = 99999999999999999999

            self.turn = random.randrange(90)
            self.accel = random.randrange(10)
            self.distance_sides = random.randrange(100)
            self.distance_front = random.randrange(100)
        else:
            self.best = (float(content[0]))
            self.bestTurn = float(content[1])
            self.bestAccel = float(content[2])
            self.bestDistanceFront = float(content[3])
            self.bestDistanceSides = float(content[4])
            self.generation = int(content[5])
            self.currentGeneration = self.generation + 1
            self.bestTime = float(content[6])

            # use 20% surrounding the best previous turn value to calc new random range
            self.turn = random.uniform(self.bestTurn - self.bestTurn / 10, self.bestTurn + self.bestTurn / 10)
            self.accel = random.uniform(self.bestAccel - self.bestAccel / 10, self.bestAccel + self.bestAccel / 10)
            self.distance_front = random.uniform(self.bestDistanceFront - self.bestDistanceFront / 10, self.bestDistanceFront + self.bestDistanceFront / 10)
            self.distance_sides = random.uniform(self.bestDistanceSides - self.bestDistanceSides / 10, self.bestDistanceSides + self.bestDistanceSides / 10)

    def mutate(self):
        #mutate with random values in a bigger margin
        self.turn = random.uniform(self.bestTurn - 20, self.bestTurn + self.bestTurn + 20)
        self.accel = random.uniform(self.bestAccel - 3, self.bestAccel + 3)
        self.distance_front = random.uniform(self.bestDistanceFront - 20, self.bestDistanceFront + 20)
        self.distance_sides = random.uniform(self.bestDistanceSides - 20, self.bestDistanceSides + 20)

    def update(self):
        if self.front_center_sensor.is_obstacle_goal:
            pass
        elif self.left_sensor.distance < self.distance_sides or self.right_sensor.distance < self.distance_sides or self.front_center_sensor.distance < self.distance_front:
            if self.left_sensor.distance < self.right_sensor.distance:
                    self.car.turn(self.turn)
            elif self.left_sensor.distance > self.right_sensor.distance:
                    self.car.turn(-self.turn)

        if self.car.speed == 0:
            self.car.accelerate(self.accel)

        if self.goal_sensor.distance < 15:
            self.car.isInGoal = True
            print("in goal")
            self.time = time.time() - self.time

        if self.goal_sensor.distance < self.best or self.time < self.bestTime and self.currentGeneration != self.generation:
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
            file.write(str(self.currentGeneration) + "\n")
            file.write(str(self.time))
            file.close()

class tinyBrainTime(Brain):
    def calcAttributes(self):
        if os.path.isfile("best1"):
            with open("best1", "r") as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                #print(content)
        self.goal_sensor = GoalSensor(self.car)
        if not os.path.isfile("best1"):
            self.best = self.goal_sensor.distance + 1
            self.bestTurn = 0
            self.bestAccel = 0
            self.bestDistance = 0
            self.generation = 0
            self.currentGeneration = 1
            self.bestTime = 99999999999999999999
            self.bestSensorAngle = 0
            self.bestSensorX = 0
            self.bestSensorY = 0

            self.turn = random.randrange(-90,90)
            self.accel = random.randrange(10)
            self.distance = random.randrange(100)
            self.sensorAngle = random.randrange(-90, 90)
            self.sensorX = random.randrange(-10, 10)
            self.sensorY = random.randrange(-15, 15)
        else:
            self.best = (float(content[0]))
            self.bestTurn = float(content[1])
            self.bestAccel = float(content[2])
            self.bestDistance = float(content[3])
            self.generation = int(content[4])
            self.currentGeneration = self.generation + 1
            self.bestTime = float(content[5])
            self.bestSensorAngle = float(content[6])
            self.bestSensorX = float(content[7])
            self.bestSensorY = float(content[8])

            # use 20% surrounding the best previous turn value to calc new random range
            self.turn = random.uniform(self.bestTurn - self.bestTurn / 10, self.bestTurn + self.bestTurn / 10)
            self.accel = random.uniform(self.bestAccel - self.bestAccel / 10, self.bestAccel + self.bestAccel / 10)
            self.distance = random.uniform(self.bestDistance - self.bestDistance / 10, self.bestDistance + self.bestDistance / 10)
            self.sensorAngle = random.uniform(self.bestSensorAngle - self.bestSensorAngle / 10, self.bestSensorAngle + self.bestSensorAngle / 10)
            self.sensorX = random.uniform(self.bestSensorX - self.bestSensorX / 10, self.bestSensorX + self.bestSensorX / 10)
            self.sensorY = random.uniform(self.bestSensorY - self.bestSensorY / 10, self.bestSensorY + self.bestSensorY / 10)

    def mutate(self):
        #mutate with random values in a bigger margin
        self.turn = random.uniform(self.bestTurn - 20, self.bestTurn + self.bestTurn + 20)
        self.accel = random.uniform(self.bestAccel - 3, self.bestAccel + 3)
        self.distance = random.uniform(self.bestDistance - 20, self.bestDistance + 20)
        self.sensorAngle = random.uniform(self.bestSensorAngle - 20, self.bestSensorAngle + 20)
        self.sensorX = random.uniform(self.bestSensorX - 20, self.bestSensorX + 20)
        self.sensorY = random.uniform(self.bestSensorY - 20, self.bestSensorY + 20)

    def setup(self):
        self.calcAttributes()
        self.sensor = Sensor(self.car, angle=self.sensorAngle, x=self.sensorX, y=self.sensorY)
        self.time = time.time()

    def update(self):
        if self.sensor.is_obstacle_goal:
            pass
        elif self.sensor.distance < self.distance:
            self.car.turn(self.turn)

        if self.car.speed == 0:
            self.car.accelerate(self.accel)

        if self.goal_sensor.distance < 15:
            self.car.isInGoal = True
            print("in goal")
            self.time = time.time() - self.time

        if self.goal_sensor.distance < self.best or self.time < self.bestTime and self.currentGeneration != self.generation:
            if os.path.isfile("best1"):
                os.remove("best1")

            self.best = self.goal_sensor.distance
            self.bestTime = self.time

            print("written")

            file = open("best1", "w")
            file.write(str(self.best) + "\n")
            file.write(str(self.turn) + "\n")
            file.write(str(self.accel) + "\n")
            file.write(str(self.distance) + "\n")
            file.write(str(self.currentGeneration) + "\n")
            file.write(str(self.bestTime) + "\n")
            file.write(str(self.sensorAngle) + "\n")
            file.write(str(self.sensorX) + "\n")
            file.write(str(self.sensorY))
            file.close()