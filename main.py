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
track = Track.level(canvas, draw_midline=True, level_number=1)
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
        population.append(Car(track, brain_level1.RandomBrain(), color="blue"))

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
    print("length: " + str(len(population)))
    # for i in range(20):
    #     population[i].update()
    #     population[i].draw()
    #print(i)
    while all([not c.isInGoal for c in population]):
        # print(fileGen())
        for c in [c for c in population]:
            if c.isalive or c.isInGoal:
                c.update()
                c.draw()
            else:
                canvas.delete(c.canvas_shape_id)
        canvas.update()
        #i += 1
    #car.update()
    #car.draw()

    # increase value to slow down total speed of simulation
    canvas.after(60, go)


# start update & mainloop of window
#i = fileGen() + 1
go()
#update()
tkinter.mainloop()
