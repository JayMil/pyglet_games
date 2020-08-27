'''
    Draw a normalized vector of length 100 towards cursor
'''

import math
import pyglet
from pyglet.shapes import Line
from numpy import array as vector

window = pyglet.window.Window(1080, 768)


def createVector(x, y):
    ''' Return a new vector '''
    return vector([x, y])

def normalize(vec, scale=1):
    ''' return vector normalized '''
    m = mag(vec)
    return createVector(vec[0]/m, vec[1]/m) * scale

def mag(vec):
    ''' Return  magnitude of vector '''
    return math.sqrt(vec[0] ** 2 + vec[1] ** 2)

def update(dt):
    global vect, nvect
    nvect = normalize(mouse - pos, 100)

@window.event
def on_mouse_motion(x, y, dx, dy):
    ''' Capture position of mouse on mouse move '''
    global mouse
    mouse = createVector(x, y)

@window.event
def on_draw():
    ''' Draw vector from center to cursor '''
    global x, y, nvect
    Line(x, y, (x+nvect[0]), (y+nvect[1])).draw()


x = window.width // 2
y = window.height // 2
pos = createVector(x, y)
mouse = createVector(x, y)
nvect = normalize(mouse - pos, 100)


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
