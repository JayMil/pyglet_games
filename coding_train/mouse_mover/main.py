'''
    Mover program to move a circle around the screen following the cursor
    using vectors, velocity and acceleration

'''
import random
import pyglet
from numpy import array as vector

from mover import Mover

FPS = 120.0
#FPS = 1.0

window = pyglet.window.Window(1080, 768)

mover = Mover(window.width // 2, window.height // 2)
window.push_handlers(mover)

@window.event
def on_draw():
    window.clear()
    mover.draw()

pyglet.clock.schedule_interval(mover.update, 1/FPS)
pyglet.app.run()
