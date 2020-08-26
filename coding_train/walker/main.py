'''
    Walker program to draw a path that moves in random directions
    using vectors

'''
import random
import pyglet
from numpy import array as vector

from walker import Walker

window = pyglet.window.Window(1080, 768)

walker = Walker(window.width // 2, window.height // 2)
@window.event
def on_draw():
    window.clear()
    walker.draw()

pyglet.clock.schedule_interval(walker.update, 1/120.0)
pyglet.app.run()
