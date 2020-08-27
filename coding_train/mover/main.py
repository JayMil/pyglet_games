'''
    Mover program to move a circle around the screen randomly
    using vectors, velocity and acceleration

'''
import random
import pyglet
from numpy import array as vector

from mover import Mover

FPS = 120.0

window = pyglet.window.Window(1080, 768)

walker = Mover(window.width // 2, window.height // 2)

@window.event
def on_draw():
    walker.draw()

pyglet.clock.schedule_interval(walker.update, 1/FPS)
pyglet.app.run()
