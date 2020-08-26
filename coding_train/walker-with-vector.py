'''
    Walker program to draw a path that moves in random directions
    using vectors

'''
import random
import pyglet
from pyglet.shapes import Rectangle
from numpy import array as vector

window = pyglet.window.Window(1080, 768)
main_batch = pyglet.graphics.Batch()

pos = vector([window.width // 2, window.height // 2])

def update(dt):
    global pos
    pos[0] += (random.randrange(3) - 1)     # range -1 through 1
    pos[1] += (random.randrange(3) - 1)     # range -1 through 1



@window.event
def on_draw():
    global pos
    #window.clear()
    #main_batch.draw()
    rec = Rectangle(pos[0], pos[1], 1, 1)
    rec.draw()

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
