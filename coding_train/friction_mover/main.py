'''
    Drop two balls of different mass
    Apply a gravity force constantly. 
    Apply a wind force when mouse is pressed

'''
import random
import pyglet
import vector

from mover import Mover

FPS = 120.0

window = pyglet.window.Window(1080, 768)


movers = []
span_padding = 50

for i in range(1, 9):
    x = random.randrange(span_padding, window.width-span_padding, 1)
    y = 200
    m = random.randrange(1, 10, 1)
    mover = Mover(x, y, window, mass=m)
    window.push_handlers(mover)
    movers.append(mover)

@window.event
def on_draw():
    window.clear()
    for mover in movers:
        mover.draw()

def update(dt):
    for mover in movers:
        mover.update(dt)

pyglet.clock.schedule_interval(update, 1/FPS)
pyglet.app.run()
