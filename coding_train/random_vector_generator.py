import random
import pyglet
from pyglet.shapes import Line
from numpy import array as vector

window = pyglet.window.Window(1080, 768)

def createVector(x, y):
    ''' Return a new vector '''
    return vector([x, y])

def createRandomVector(length):
    ''' Return a random vector within a given length '''
    x = (length*2) * random.random() - length
    y = (length*2) * random.random() - length
    return createVector(x, y)


def update(dt):
    ''' Create new random vector '''
    global vect
    vect = createRandomVector(100)

@window.event
def on_draw():
    ''' Draw line from center to random vector point '''
    global x, y, nvect
    Line(x, y, (x+vect[0]), (y+vect[1])).draw()



x = window.width // 2
y = window.height // 2

vect = createRandomVector(100)

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
