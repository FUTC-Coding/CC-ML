#
# MAIN PROGRAM
#
# Execute this script to start the simulation:
#    py main.py
#
import tkinter
from lib.tracks import Track
from lib.car import Car
import brain_level1
import os
import time

# global best
# global bestTurn
# global bestAccel
# global bestDistanceSides
# global bestDistanceFront
#
# def getBest():
#     return best
#
# def getBestTurn():
#     return bestTurn
#
# def getBestAccel():
#     return bestAccel
#
# def getBestDistanceSides():
#     return bestDistanceSides
#
# def getBestDistanceFront():
#     return bestDistanceFront

# create canvas for drawing
canvas = tkinter.Canvas(width=800, height=600, background="yellow green")
canvas.pack()

# load track
track = Track.level(canvas, draw_midline=True, level_number=4)
track.draw()

# create car
#car = Car(track, brain_level1.SensorBrain(), color="blue")
population = []
def populate():
    if population:
        for c in [c for c in population]:
            canvas.delete(c.canvas_shape_id)
        del population[:]
    for i in range(20):
        population.append(Car(track, brain_level1.tinyBrainTime(), color="blue"))

def setAttributes():
    for p in population:
        p.brain.calcAttributes()

def mutate():
    for i in range(5):
        population[i].brain.mutate()

#def update():
#    '''Update the car and redraw it.'''
#    for i in range(20):
#        population[i].update()
#        population[i].draw()
def fileGen():
    if os.path.isfile("best"):
        with open("best", "r") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            return  int(content[5])
    else:
        return 0



def go():
    populate()
    setAttributes()
    mutate()

    print("length: " + str(len(population)))
    time1 = 0
    time1 = time.time()
    # for i in range(20):
    #     population[i].update()
    #     population[i].draw()
    #print(i)
    time2 = 0
    while all([not c.isInGoal for c in population]) and any([c.isalive for c in population]) and time2 < 60:
        time2 = time.time() - time1
        if time2 < 60:
            # print(fileGen())
            for c in [c for c in population]:
                if c.isalive or c.isInGoal:
                    c.update()
                    c.draw()
                else:
                    canvas.delete(c.canvas_shape_id)
                    #for c in c.sensors:
                    #    canvas.delete((c.sensor_line_id))
        else:
            for c in [c for c in population]:
                canvas.delete(c.canvas_shape_id)
                #for c in c.sensors:
                    #canvas.delete((c.sensor_line_id))

        canvas.update()
        print(time2)
        #i += 1
    #car.update()
    #car.draw()

    # increase value to slow down total speed of simulation
    canvas.after(1, go)


# start update & mainloop of window
#i = fileGen() + 1
go()
#update()
tkinter.mainloop()
