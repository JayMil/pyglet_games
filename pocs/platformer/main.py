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


x = random.randrange(50, window.width-50, 1)
y = 200
m = 4
mover = Mover(x, y, window, mass=m)
window.push_handlers(mover)

@window.event
def on_draw():
    window.clear()
    mover.draw()

def update(dt):
    mover.update(dt)

pyglet.clock.schedule_interval(update, 1/FPS)
pyglet.app.run()
